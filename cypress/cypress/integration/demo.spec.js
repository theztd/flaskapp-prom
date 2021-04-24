describe('Title page works', function (){
    beforeEach(() => {
        cy.visit('https://flaskapp.fejk.net')
    })

    it('Check title', function() {
        cy.url().should('include', 'flaskapp')

        cy.contains("Mate stesti!!!")

    })

})    
