variable "fqdn" {
  type = string
  default = "flaskapp.fejk.net"
}

variable "dcs" {
  type = list(string)
  default = ["dc1", "devel"]
}

variable "api_image" {
  type = string
  default = "theztd/flaskapp:latest"
}

job "flaskapp" {
    datacenters = var.dcs

    group "fe" {
        count = 1
        
        network {
            port "http" { to = 80 }
            port "api" { to = 5000 }
        }
        
        service {
            name = "${JOB}-http"

            tags = [
                "public",
                "traefik.enable=true",
                "traefik.http.routers.${NOMAD_JOB_NAME}-http.rule=Host(`${var.fqdn}`)",
            ]

            port = "http"


            check {
                name = "${NOMAD_JOB_NAME} - alive"
                type = "http"
                path = "/"
                interval = "1m"
                timeout = "10s"

                # Task should run 2m after deployment
                check_restart {
                    limit = 5
                    grace = "2m"
                    ignore_warnings = true
                }
            }
         }
        
        task "nginx" {
            driver = "docker"

            config {
                image   = "nginx"
                ports = [ "http" ]
                
                mount {
                    type = "volume"
                    source = "data-${var.fqdn}"
                    target = "/usr/share/nginx/html"
                    readonly = false
                    volume_options {
                        labels {
                            job = "${NOMAD_JOB_NAME}"
                            domain = "${var.fqdn}"
                        }
                    }
                }
            }
            
            resources {
                cpu = 100
                memory = 64
            }
        } # END task nginx

        task "flaskapp" {
          driver = "docker"

          config {
            image = var.api_image
            ports = ["api"]
            labels {
              group = "flask"
            }
            command = "--port 5000 main:app"
          }
          
          resources {
            cpu = 200
            memory = 64
          }
        
        }

    } # END group FE

}
