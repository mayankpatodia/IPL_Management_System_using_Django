from django.db import models

# Create your models here.
class Team(models.Model):
    team_id = models.DecimalField(max_digits=2,primary_key=True,decimal_places=0)
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    coach = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    captain = models.CharField(max_length=50)
    logo_url = models.ImageField(upload_to='', default='default.png')
    profile_url = models.ImageField(upload_to='', default='default.png')
    cover_url = models.ImageField(upload_to='', default='default.png')

    def __str__(self):
        s = str(self.team_id) + "," + str(self.code) + "," + str(self.name) + "," + str(self.coach) + "," + str(self.owner) + "," + str(self.captain) + "," + str(self.logo_url)
        return s

class Player(models.Model):
    player_id = models.DecimalField(max_digits=2,primary_key=True,decimal_places=0)
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    runs = models.DecimalField(max_digits=5,decimal_places=0)
    wickets = models.DecimalField(max_digits=5,decimal_places=0)
    team = models.ForeignKey(Team,on_delete=models.CASCADE)

    def __str__(self):
        #s = str(self.player_id) + "," + str(self.name) + "," + str(self.role) + "," + str(self.runs) + "," + str(self.wickets) + "," + str(self.team)
        return self.name

class Venue(models.Model):
    venue_id = models.DecimalField(max_digits=2,primary_key=True,decimal_places=0)
    name = models.CharField(max_length=50)
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    image_url = models.CharField(max_length=50)

    def __str__(self):
        #s = str(self.venue_id) + "," + str(self.name) + "," + str(self.team) + "," + str(self.image_url)
        return self.name

class Match(models.Model):
    match_id = models.DecimalField(max_digits=2,primary_key=True,decimal_places=0)
    date = models.DateField()
    time = models.TimeField()
    team1 = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='team_one')
    team2 = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='team_two')
    venue_id = models.ForeignKey(Venue,on_delete=models.CASCADE)
    team1_score = models.CharField(max_length=50, null=True, blank=True)
    team2_score = models.CharField(max_length=50, null=True, blank=True)
    team1_overs = models.CharField(max_length=50, null=True, blank=True)
    team2_overs = models.CharField(max_length=50, null=True, blank=True)
    result = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        #s = str(self.match_id) + "," + str(self.date) + "," + str(self.time) + "," + str(self.team1) + "," + str(self.team2) + "," + str(self.venue_id)
        s = str(self.date) + "," + str(self.time) + "," + str(self.team1) + "," + str(self.team2) + "," + str(self.venue_id)
        return s

class Statistics(models.Model):
    statistics_id = models.DecimalField(max_digits=2,primary_key=True,decimal_places=0)
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    played = models.DecimalField(max_digits=5,decimal_places=0)
    won = models.DecimalField(max_digits=5,decimal_places=0)
    lost = models.DecimalField(max_digits=5,decimal_places=0)
    tied = models.DecimalField(max_digits=5,decimal_places=0)
    points = models.DecimalField(max_digits=5,decimal_places=0)

    def __str__(self):
        s = str(self.statistics_id) + "," + str(self.team) + "," + str(self.played) + "," + str(self.won) + "," + str(self.lost) + "," + str(self.tied) + "," + str(self.points)
        return s

class Enquiries(models.Model):
    subject = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    message = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        s = str(self.subject) + "," + str(self.name) + "," + str(self.email) + "," + str(self.message)
        return s

#
# class Messages(models.Model):
#     name = models.CharField(max_length=100, null=True, blank=True)
#     email = models.CharField(max_length=100, null=True, blank=True)
#     message = models.CharField(max_length=100, null=True, blank=True)
#
#     def __str__(self):
#         s = str(self.message) + "," + str(self.name) + "," + str(self.email) + "," + str(self.message)
#         return s
