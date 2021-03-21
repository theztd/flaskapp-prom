job "flaskapp" {
    datacenters = ["dc1"]

    group "fe" {
        task "nginx" {
            driver = "docker"

            config {
                image   = "nginx"
            }

        }

    }

}
