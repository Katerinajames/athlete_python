class Athlete:
	
                
       
        
	def __str__(self):
		print("Name :%s , Birthdate:%s ,Sportsname:%s,Score:%d, Worldrank:%d,Countparticipation:%d"%(self.get_name(),self.get_birthdate(),self.get_sportsname(),self.get_score(),self.get_worldrank(),self.get_CountParticipation()))	
	def __init__(self,name,birthdate,sportsname,score, worldrank,countParticipation):
		self.name=name
		self.birthdate=birthdate
		self.sportsname=sportsname
		self.score=score
		self.worldrank=worldrank 
		self.countParticipation=countParticipation 
	def set_name(self,name): 
         self.name=name	 	        	
	def set_birthdate(self ,birthdate): 
         self.birthdate=birthdate     
	def set_sportsname(self,sportsname): 
         self.sportsname=sportsname	
	def set_score(self ,score): 
         self.score=score 	
	def set_worldrank(self ,worldrank): 
         self.worldrank=worldrank	  	
	def set_CountParticipation(self ,countParticipation): 
          self.countParticipation=countParticipation	      	 	      
	def get_name  (self ): 
         return self.name 	                
	def get_birthdate(self): 
         return self.birthdate 	
	def get_sportsname(self ): 
         return self.sportsname 	
	def get_score(self ): 
         return self.score
	def get_worldrank(self): 
         return  self.worldrank
	def get_CountParticipation(self): 
         return self.countParticipation               
	def increase_CountParticipation(self): 
         r=self.get_CountParticipation()+1
         return r
	def athleteScoreRecordLimit(self, recordLimit,  game):
	 if game == "TRIPLOUN":
	        
               if   self.get_score() > recordLimit: 
                 print ("Our athlete will participate in the sport event")
               else:
                  print ("Our athlete will not participate in the sport event") 
	 if  game == "M100": 
            if (self.get_score() >recordLimit): 
                 print("Our athlete will participate in the sport event")
            else:
                  print ("Our athlete will not participate in the sport event")
             
           	
print("-----------------------------------------------------------")   	
		
print("ATHLETE a1  INFO")		  
a1 =Athlete("Lewis","01/07/1961", "M100",2,2,3)
a1.__str__()  
print("-----------------------------------------------------------")  
print("ATHLETE a2  INFO")
            
a2 =Athlete("Jones","01/08/1962", "TRIPLOUN",2,2,3)
a2.__str__()                 
       
print("-----------------------------------------------------------") 
print ("Call method athleteScoreRecordLimit  to check if our athlete (a1) can participate in M100")


a1.athleteScoreRecordLimit(1,"M100")

print("-----------------------------------------------------------")
print ("Call method athleteScoreRecordLimit  to check if our athlete (a2) can participate in TRIPLOUN")  
              
                
a2.athleteScoreRecordLimit(1.50,"TRIPLOUN")

