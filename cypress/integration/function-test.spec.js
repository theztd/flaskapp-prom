describe('Test core features',  () => {
    beforeEach( () => {
        cy.visit(Cypress.env('APP_URL'))
    })

    it('Check title', () => {
        //cy.url().should('include', 'flaskapp')

        cy.contains("API responser")

    })

    it('Check GraphQL button', () => {
        cy.get("[test-data=graphql-api]").click()
        cy.url().should('include', 'graphql')
        cy.get(".title").contains("Graph")
        
        // Test query in editor and check result
        cy.get(".query-editor").type('query {{}version{}}')
        cy.get(".execute-button").click()
        cy.get(".result-window").contains('"version":')

    })

    it('Check REST API text', () => {
        cy.get("[test-data=rest-api-txt]").click()
        cy.url().should('include', 'url1')
        cy.contains("You waited")
    })

    it('Check REST API json', () => {
        cy.get("[test-data=rest-api-json]").click()
        cy.url().should('include', 'url1.json')
        cy.contains('"wait_time":')
    })
})    
