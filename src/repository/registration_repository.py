class RegistrationRepository:
    def __init__(self, db):
        self.db = db

    def signUpCompany(self, body):
        self.db.signUpCompany(body)
        r = body
        return r
    
    def signUpUser(self, body):
        return self.db.signUpUser(body)
    
    def login(self, body):
        return self.db.login(body)
    
    def loginCompany(self, body):
        return self.db.loginCompany(body)
    
    def loginAdmin(self, body):
        return self.db.loginAdmin(body)
    
    def getCompany(self, body):
        return self.db.getCompany(body)
    
    def getUser(self, body):
        return self.db.getUser(body)
    
    def getCompanyUser(self, body):
        return self.db.getCompanyUser(body)
    
    def getCompanyUsers(self, body):
        return self.db.getCompanyUsers(body)
    
    def getCompanyUserByCompany(self, body):
        return self.db.getCompanyUserByCompany(body)
    
    def getCompanyUserByUser(self, body):
        return self.db.getCompanyUserByUser(body)
    
    def getCompanyUserByCompanyAndUser(self, body):
        return self.db.getCompanyUserByCompanyAndUser(body)