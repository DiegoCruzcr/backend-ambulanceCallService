from src.repository.registration_repository import RegistrationRepository


class RegistrationService:
    def __init__(self, repository: RegistrationRepository):
        self.repository = repository

    def signUpCompany(self, body):
        self.repository.signUpCompany(body)
        r = body
        return r
    
    def signUpUser(self, body):
        self.repository.signUpUser(body)
        r = body
        return r
    
    def login(self, body):
        user = self.repository.getUser(body)
        if body['password'] == user['password']:
            return user
        else:
            return None
    
    def loginCompany(self, body):
        company = self.repository.getCompany(body)
        if body['password'] == company['password']:
            return company
        else:
            return None
    
    def loginAdmin(self, body):
        return self.repository.loginAdmin(body)
    
    def getCompany(self, body):
        return self.repository.getCompany(body)
    
    def getUser(self, body):
        return self.repository.getUser(body)
    
    def getCompanyUser(self, body):
        return self.repository.getCompanyUser(body)
    
    def getCompanyUsers(self, body):
        return self.repository.getCompanyUsers(body)
    
    def getCompanyUserByCompany(self, body):
        return self.repository.getCompanyUserByCompany(body)
    
    def getCompanyUserByUser(self, body):
        return self.repository.getCompanyUserByUser(body)
    
    def getCompanyUserByCompanyAndUser(self, body):
        return self.repository.getCompanyUserByCompanyAndUser(body)
    
    def getCompanyUserByCompanyAndUserAndRole(self, body):
        return self.repository.getCompanyUserByCompanyAndUserAndRole(body)
    
    def getCompanyUserByCompanyAndRole(self, body):
        return self.repository.getCompanyUserByCompanyAndRole(body)
    
    def getCompanyUserByUserAndRole(self, body):
        return self.repository.getCompanyUserByUserAndRole(body)
    
    def getCompanyUserByRole(self, body):
        return self.repository.getCompanyUserByRole(body)
    
    def getCompanyUserByCompanyAndUserAndRoleAndStatus(self, body):
        return self.repository.getCompanyUserByCompanyAndUserAndRoleAndStatus(body)
    
    def getCompanyUserByCompanyAndRoleAndStatus(self, body):
        return self.repository.getCompanyUserByCompanyAndRoleAndStatus(body)
    
    def getCompanyUserByUserAndRoleAndStatus(self, body):
        return self.repository.getCompanyUserByUserAndRoleAndStatus(body)
    
    def getCompanyUserByRoleAndStatus(self, body):
        return self.repository.getCompanyUserByRoleAndStatus(body)
    
    def getCompanyUserByCompanyAndUserAndStatus(self, body):
        return self.repository.getCompanyUserByCompanyAndUserAndStatus(body)