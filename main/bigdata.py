import time

start1 = time.time()
def bubblesort(A):
    '''
    (list) -> (list)
    This Function takes in a classlist, and sorts it using the bubble sort method.
    (list) -> (list)
    
    '''
    for i in range(len(A)):
        for k in range(len(A) - 1,i,-1):
            if (A[k].asciiname<A[k - 1].asciiname): 
                swap(A,k,k - 1)
def swap(A,a,b):
    
    '''$
    (list,int,int) -> (list)
    This Function is a helper function for the BubbleSort Function
       
    '''    
    tmp = A[a]
    A[a] = A[b]
    A[b] = tmp
    
    
def chunks(l, n): 
    
    '''
    (List, int) => (list)
    This Function takes in an list, and splits that array into a 2d array by chunk size.
           
    '''       
    return [l[i:i+n] for i in range(0, len(l), n)]

while 1:
    size = 19
    break
    
        

# creating all the variables for use
oneline = []
a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
io = [] # io instead of i, because i always use for i in range.....
j = []
k = []
l = []
m = []
n = []
o = []
p = []
q = []
r = []
s = []
t = []
u = []
v = []
w = []
x = []
y = []
z = []
unique =[]

with open("tester.txt", encoding = 'utf-8') as i: # opening the file
    print('Reading lines please wait...')
    start = time.time() # timing 
    lines = i.readlines()
    end = time.time()
    elapsed = end - start
    print('Time Taken: ' + str(elapsed))
lenlines = (len(lines))
print('Removing Newline Characters, Please wait...')
start = time.time()
for i in range(0,len(lines)):
    lines[i] = lines[i][:-1] 
end = time.time()
elapsed = end - start
print('Time Taken: ' + str(elapsed))

print('Filling Arrays, please wait... ')
start = time.time()

def fillingarray(array,search,textname):
    '''
    (list,string,string) -> (file, list)
    This function fills and array by starting letter, and writes it to a file.
    '''
    for i in range(0, lenlines):  
        oneline = lines[i].split("\t")
        if (oneline[1][0]) == search:
            array.append(oneline)

    with open(textname, 'w', encoding = 'utf-8') as file:
        for i in range(0, len(array)):
            for kx in range (0,len(array[i])):
                file.write(array[i][kx] + "\n") 
              

fillingarray(a,"A",'a.txt') #using the function to write the files
a = []
fillingarray(b,"B",'b.txt')
b = []
fillingarray(c,"C",'c.txt')
c = []
fillingarray(d,"D",'d.txt')
d = []
fillingarray(e,"E",'e.txt')
e = []
fillingarray(f,"F",'f.txt')
f = []
fillingarray(g,"G",'g.txt')
g = []
fillingarray(h,"H",'h.txt')
h = []
fillingarray(io,"I",'io.txt')
io = []
fillingarray(j,"J",'j.txt')
j = []
fillingarray(k,"K",'k.txt')
k = []
fillingarray(l,"L",'l.txt')
l = []
fillingarray(m,"M",'m.txt')
m = []
fillingarray(n,"N",'n.txt')
n = []
fillingarray(o,"O",'o.txt')
o = []
fillingarray(p,"P",'p.txt')
p = []
fillingarray(q,"Q",'q.txt')
q = []
fillingarray(r,"R",'r.txt')
r = []
fillingarray(s,"S",'s.txt')
s = []
fillingarray(t,"T",'t.txt')
t = []
fillingarray(u,"U",'u.txt')
u = []
fillingarray(v,"V",'v.txt')
v = []
fillingarray(w,"W",'w.txt')
w = []
fillingarray(x,"X",'x.txt')
x = []
fillingarray(y,"Y",'y.txt')
y = []
fillingarray(z,"Z",'z.txt')
z = []
print(a)

#for i in range(0, lenlines):  
    #oneline = lines[i].split("\t")
    #if (oneline[1][0]) == 'A':
        #a.append(oneline)
    
end = time.time()   
elapsed = end - start
print('Time Taken: ' + str(elapsed)) #measuring time again


print('Writing html Files, please wait:')
start = time.time()
with open("a.txt", 'r', encoding = 'utf-8') as file: # opening file a, and re inserting it into an array. This is done to save RAM
    lines = file.readlines()
    holder = []
    counter = 0
    for i in range(0,len(lines)):
        lines[i] = lines[i][:-1]           
    for i in range(0,len(lines)):
            holder.append(lines[i])
    a = chunks(holder, 19)        
#creating the class
class Information:
    def __init__(self, geonameid, name, asciiname, alternatenames, latitude, longitude, featureclass,
                 featurecode, countrycode, cc2, admin1code, admin2code, admin3code, admin4code,
                 population, elevation, dem, timezone, modificationdate):
        '''
        (self, int, string, string, string, string, string, string, string, string, string, string, string, string, string, string, string, string, string, string, string)
         
        This method takes items and puts it in corresponding instance varibles.
        '''        
        self.position = Position(latitude, longitude)
        self.geonameid = geonameid
        self.name = name
        self.asciiname = asciiname
        self.alternatenames = alternatenames
        self.featureclass = featureclass
        self.featurecode = featurecode
        self.countrycode = countrycode
        self.cc2 = cc2
        self.admin1code = admin1code
        self.admin2code = admin2code
        self.admin3code = admin3code
        self.admin4code = admin4code
        self.population = population
        self.elevation = elevation
        self.dem = dem
        self.timezone = timezone
        self.modificationdate = modificationdate
        
    
    def __str__(self):
        '''
        (self) -> (string)
         
        This method takes self and makes it a string 
        '''           
        return(self.geonameid + self.name + self.asciiname + self.alternatenames +self.position.latitude +self.position.longitude + self.featureclass + self.featurecode + self.countrycode + self.cc2 + self.admin1code + self.admin2code + self.admin3code + self.admin4code + self.population + self.elevation + self.dem + self.timezone + self.modificationdate)
#creating another class    
class Position:
    '''
    (self, string , string)
    This method takes items and puts it in corresponding instance varibles.
    '''
    def __init__(self,latitude, longitude):
        
        self.latitude = latitude
        self.longitude = longitude
        
    
classlist = []

for i in range(0,len(a)):
    classlist.append(Information(a[i][0],a[i][1],a[i][2],a[i][3],a[i][4],a[i][5],a[i][6],a[i][7], a[i][8], a[i][9], # takes an array and puts it into the class information
                     a[i][10], a[i][11], a[i][12], a[i][13], a[i][14], a[i][15], a[i][16], a[i][17], a[i][18]))
bubblesort(classlist) # sort the objects


def writingfile(input):
    filename1 =  str(input)
    with open(filename1, 'w', encoding = 'utf-8') as file: # writing the file
        file.write(
            "<style>" + "\n"
            
            "body, html {" "\n"
             "eight: 100%;" "\n"
              "width: 100%;" "\n"
            "}" "\n"
            
            "</style>" "\n"
            
            "<!DOCTYPE html>" "\n"
            "<html> " "\n"
            "<head> " "\n"
              "<meta http-equiv=\"content-type\" content=\"text/html; charset=UTF-8\" /> " "\n" # all this pre emptive code is taken from the google maps api website
              "<title>Google Maps Multiple Markers</title> " "\n"
              "<script src=\"http://maps.google.com/maps/api/js?sensor=false\" " "\n"
                      "type=\"text/javascript\"></script>" "\n"
            '</head>'  "\n"
            '<body>' "\n"
                    
              '<div id="map" style="width: 100%; height: 100%;"></div>' "\n"
                 '  <script type="text/javascript">' "\n"   
                 '    var locations = [' "\n"   
                   ) 
        for i in range(0,len(classlist)):
            if i < len(classlist)-1:
                file.write( '      [' + '\"' + (str(classlist[i].asciiname) +  '\"') +',' + str(classlist[i].position.longitude) + ',' +  str(classlist[i].position.latitude) + ',' + str(i+1) + '],'   + '\n')
            if i == len(classlist)-1:
                file.write( '      [' + '\"' + (str(classlist[i].asciiname) +  '\"') +',' + str(classlist[i].position.longitude) + ',' +  str(classlist[i].position.latitude) + ',' + str(i+1) + ']'   + '\n') # writting information the way needed
        
        file.write(
           '];' "\n"
            
                'var map = new google.maps.Map(document.getElementById(\'map\'), {' "\n"
                  'zoom: 2,' "\n"
                  'center: new google.maps.LatLng(0, 0),' "\n"
                  'mapTypeId: google.maps.MapTypeId.ROADMAP' "\n"
                '});' "\n"
             
                'var infowindow = new google.maps.InfoWindow();' "\n"
             
                'var marker, i;' "\n"
            
               ' for (i = 0; i < locations.length; i++) { '  "\n"
                  'marker = new google.maps.Marker({' "\n"
                   ' position: new google.maps.LatLng(locations[i][1], locations[i][2]),' "\n"
                    'map: map' "\n"
                '  });' "\n"
            
                  'google.maps.event.addListener(marker, \'click\', (function(marker, i) {' "\n" 
                    'return function() {' "\n"
                      'infowindow.setContent(locations[i][0]);' "\n"
                      'infowindow.open(map, marker);' "\n"
                    '}' "\n"
                 ' })(marker, i));' "\n"
                '}' "\n"
              '</script>' "\n"
            '</body>' "\n"
           ' </html> ' "\n" )
        
        return ('file complete')
    
    
writingfile('a.html')   
with open("b.txt", 'r', encoding = 'utf-8') as file:
    lines = file.readlines()
    holder = []
    counter = 0
    for i in range(0,len(lines)): # removing /n
        lines[i] = lines[i][:-1]           
    for i in range(0,len(lines)):
            holder.append(lines[i])
    b = chunks(holder, 19)
    
for i in range(0,len(b)):
    classlist.append(Information(b[i][0],b[i][1],b[i][2],b[i][3],b[i][4],b[i][5],b[i][6],b[i][7], b[i][8], b[i][9],
                     b[i][10], b[i][11], b[i][12], b[i][13], b[i][14], b[i][15], b[i][16], b[i][17], b[i][18]))
bubblesort(classlist)    

writingfile('b.html')
b = []
classlist = []

with open("c.txt", 'r', encoding = 'utf-8') as file:
    lines = file.readlines()
    holder = []
    counter = 0
    for i in range(0,len(lines)):
        lines[i] = lines[i][:-1]           
    for i in range(0,len(lines)):
            holder.append(lines[i])
    c = chunks(holder, 19)
    
for i in range(0,len(c)):
    classlist.append(Information(c[i][0],c[i][1],c[i][2],c[i][3],c[i][4],c[i][5],c[i][6],c[i][7], c[i][8], c[i][9],
                     c[i][10], c[i][11], c[i][12], c[i][13], c[i][14], c[i][15], c[i][16], c[i][17], c[i][18]))
bubblesort(classlist)    

writingfile('c.html') 
c=[]
classlist = []


with open("d.txt", 'r', encoding = 'utf-8') as file:
    lines = file.readlines()
    holder = []
    counter = 0
    for i in range(0,len(lines)):
        lines[i] = lines[i][:-1]           
    for i in range(0,len(lines)):
            holder.append(lines[i])
    d = chunks(holder, 19)
    
for i in range(0,len(d)):
    classlist.append(Information(d[i][0],d[i][1],d[i][2],d[i][3],d[i][4],d[i][5],d[i][6],d[i][7], d[i][8], d[i][9],
                     d[i][10], d[i][11], d[i][12], d[i][13], d[i][14], d[i][15], d[i][16], d[i][17], d[i][18]))
bubblesort(classlist)    

writingfile('d.html') 
classlist = []

d =[]

with open("e.txt", 'r', encoding = 'utf-8') as file:
    lines = file.readlines()
    holder = []
    counter = 0
    for i in range(0,len(lines)):
        lines[i] = lines[i][:-1]           
    for i in range(0,len(lines)):
            holder.append(lines[i])
    e = chunks(holder, 19)
    
for i in range(0,len(e)):
    classlist.append(Information(e[i][0],e[i][1],e[i][2],e[i][3],e[i][4],e[i][5],e[i][6],e[i][7], e[i][8], e[i][9],
                     e[i][10], e[i][11], e[i][12], e[i][13], e[i][14], e[i][15], e[i][16], e[i][17], e[i][18]))
bubblesort(classlist)    

writingfile('e.html') 
classlist = []

e =[]
with open("f.txt", 'r', encoding = 'utf-8') as file:
    lines = file.readlines()
    holder = []
    counter = 0
    for i in range(0,len(lines)):
        lines[i] = lines[i][:-1]           
    for i in range(0,len(lines)):
            holder.append(lines[i])
    f = chunks(holder, 19)
    
for i in range(0,len(f)):
    classlist.append(Information(f[i][0],f[i][1],f[i][2],f[i][3],f[i][4],f[i][5],f[i][6],f[i][7], f[i][8], f[i][9],
                     f[i][10], f[i][11], f[i][12], f[i][13], f[i][14], f[i][15], f[i][16], f[i][17], f[i][18]))
bubblesort(classlist)    

writingfile('f.html') 
classlist = []

f =[]
with open("g.txt", 'r', encoding = 'utf-8') as file:
    lines = file.readlines()
    holder = []
    counter = 0
    for i in range(0,len(lines)):
        lines[i] = lines[i][:-1]           
    for i in range(0,len(lines)):
            holder.append(lines[i])
    g = chunks(holder, 19)
    
for i in range(0,len(g)):
    classlist.append(Information(g[i][0],g[i][1],g[i][2],g[i][3],g[i][4],g[i][5],g[i][6],g[i][7], g[i][8], g[i][9],
                     g[i][10], g[i][11], g[i][12], g[i][13], g[i][14], g[i][15], g[i][16], g[i][17], g[i][18]))
bubblesort(classlist)    

writingfile('g.html') 
classlist = []
g =[]

with open("h.txt", 'r', encoding = 'utf-8') as file:
    lines = file.readlines()
    holder = []
    counter = 0
    for i in range(0,len(lines)):
        lines[i] = lines[i][:-1]           
    for i in range(0,len(lines)):
            holder.append(lines[i])
    h = chunks(holder, 19)
    
for i in range(0,len(h)):
    classlist.append(Information(h[i][0],h[i][1],h[i][2],h[i][3],h[i][4],h[i][5],h[i][6],h[i][7], h[i][8], h[i][9],
                     h[i][10], h[i][11], h[i][12], h[i][13], h[i][14], h[i][15], h[i][16], h[i][17], h[i][18]))
bubblesort(classlist)    

writingfile('h.html') 
classlist = []
h =[]

with open("io.txt", 'r', encoding = 'utf-8') as file:
    lines = file.readlines()
    holder = []
    counter = 0
    for i in range(0,len(lines)):
        lines[i] = lines[i][:-1]           
    for i in range(0,len(lines)):
            holder.append(lines[i])
    io = chunks(holder, 19)
    
for i in range(0,len(io)):
    classlist.append(Information(io[i][0],io[i][1],io[i][2],io[i][3],io[i][4],io[i][5],io[i][6],io[i][7], io[i][8], io[i][9],
                     io[i][10], io[i][11], io[i][12], io[i][13], io[i][14], io[i][15], io[i][16], io[i][17], io[i][18]))
bubblesort(classlist)    

writingfile('io.html') 
classlist = []
io =[]
with open("j.txt", 'r', encoding = 'utf-8') as file:
    lines = file.readlines()
    holder = []
    counter = 0
    for i in range(0,len(lines)):
        lines[i] = lines[i][:-1]           
    for i in range(0,len(lines)):
            holder.append(lines[i])
    j = chunks(holder, 19)
    
for i in range(0,len(j)):
    classlist.append(Information(j[i][0],j[i][1],j[i][2],j[i][3],j[i][4],j[i][5],j[i][6],j[i][7], j[i][8], j[i][9],
                     j[i][10], j[i][11], j[i][12], j[i][13], j[i][14], j[i][15], j[i][16], j[i][17], j[i][18]))
bubblesort(classlist)    

writingfile('j.html') 
classlist = []
j= []

with open("k.txt", 'r', encoding = 'utf-8') as file:
    lines = file.readlines()
    holder = []
    counter = 0
    for i in range(0,len(lines)):
        lines[i] = lines[i][:-1]           
    for i in range(0,len(lines)):
            holder.append(lines[i])
    k = chunks(holder, 19)
    
for i in range(0,len(k)):
    classlist.append(Information(k[i][0],k[i][1],k[i][2],k[i][3],k[i][4],k[i][5],k[i][6],k[i][7], k[i][8], k[i][9],
                     k[i][10], k[i][11], k[i][12], k[i][13], k[i][14], k[i][15], k[i][16], k[i][17], k[i][18]))
bubblesort(classlist)    

writingfile('k.html') 
classlist = []
k =[]

with open("l.txt", 'r', encoding = 'utf-8') as file:
    lines = file.readlines()
    holder = []
    counter = 0
    for i in range(0,len(lines)):
        lines[i] = lines[i][:-1]           
    for i in range(0,len(lines)):
            holder.append(lines[i])
    l = chunks(holder, 19)
    
for i in range(0,len(l)):
    classlist.append(Information(l[i][0],l[i][1],l[i][2],l[i][3],l[i][4],l[i][5],l[i][6],l[i][7], l[i][8], l[i][9],
                     l[i][10], l[i][11], l[i][12], l[i][13], l[i][14], l[i][15], l[i][16], l[i][17], l[i][18]))
bubblesort(classlist)    

writingfile('l.html') 
classlist = []
l =[]
with open("m.txt", 'r', encoding = 'utf-8') as file:
    lines = file.readlines()
    holder = []
    counter = 0
    for i in range(0,len(lines)):
        lines[i] = lines[i][:-1]           
    for i in range(0,len(lines)):
            holder.append(lines[i])
    m = chunks(holder, 19)
    
for i in range(0,len(m)):
    classlist.append(Information(m[i][0],m[i][1],m[i][2],m[i][3],m[i][4],m[i][5],m[i][6],m[i][7], m[i][8], m[i][9],
                     m[i][10], m[i][11], m[i][12], m[i][13], m[i][14], m[i][15], m[i][16], m[i][17], m[i][18]))
bubblesort(classlist)    

writingfile('m.html') 
classlist = []
m =[]
with open("n.txt", 'r', encoding = 'utf-8') as file:
    lines = file.readlines()
    holder = []
    counter = 0
    for i in range(0,len(lines)):
        lines[i] = lines[i][:-1]           
    for i in range(0,len(lines)):
            holder.append(lines[i])
    n = chunks(holder, 19)
    
for i in range(0,len(n)):
    classlist.append(Information(n[i][0],n[i][1],n[i][2],n[i][3],n[i][4],n[i][5],n[i][6],n[i][7], n[i][8], n[i][9],
                     n[i][10], n[i][11], n[i][12], n[i][13], n[i][14], n[i][15], n[i][16], n[i][17], n[i][18]))
bubblesort(classlist)    

writingfile('n.html') 
classlist = []
n =[]
with open("o.txt", 'r', encoding = 'utf-8') as file:
    lines = file.readlines()
    holder = []
    counter = 0
    for i in range(0,len(lines)):
        lines[i] = lines[i][:-1]           
    for i in range(0,len(lines)):
            holder.append(lines[i])
    o = chunks(holder, 19)
    
for i in range(0,len(o)):
    classlist.append(Information(o[i][0],o[i][1],o[i][2],o[i][3],o[i][4],o[i][5],o[i][6],o[i][7], o[i][8], o[i][9],
                     o[i][10], o[i][11], o[i][12], o[i][13], o[i][14], o[i][15], o[i][16], o[i][17], o[i][18]))
bubblesort(classlist)    

writingfile('o.html') 
classlist = []
o =[]
with open("p.txt", 'r', encoding = 'utf-8') as file:
    lines = file.readlines()
    holder = []
    counter = 0
    for i in range(0,len(lines)):
        lines[i] = lines[i][:-1]           
    for i in range(0,len(lines)):
            holder.append(lines[i])
    p = chunks(holder, 19)
    
for i in range(0,len(p)):
    classlist.append(Information(p[i][0],p[i][1],p[i][2],p[i][3],p[i][4],p[i][5],p[i][6],p[i][7], p[i][8], p[i][9],
                     p[i][10], p[i][11], p[i][12], p[i][13], p[i][14], p[i][15], p[i][16], p[i][17], p[i][18]))
bubblesort(classlist)    

writingfile('p.html') 
classlist = []
p =[]
with open("q.txt", 'r', encoding = 'utf-8') as file:
    lines = file.readlines()
    holder = []
    counter = 0
    for i in range(0,len(lines)):
        lines[i] = lines[i][:-1]           
    for i in range(0,len(lines)):
            holder.append(lines[i])
    q = chunks(holder, 19)
    
for i in range(0,len(q)):
    classlist.append(Information(q[i][0],q[i][1],q[i][2],q[i][3],q[i][4],q[i][5],q[i][6],q[i][7], q[i][8], q[i][9],
                     q[i][10], q[i][11], q[i][12], q[i][13], q[i][14], q[i][15], q[i][16], q[i][17], q[i][18]))
bubblesort(classlist)    

writingfile('q.html') 
classlist = []
q =[]
with open("r.txt", 'r', encoding = 'utf-8') as file:
    lines = file.readlines()
    holder = []
    counter = 0
    for i in range(0,len(lines)):
        lines[i] = lines[i][:-1]           
    for i in range(0,len(lines)):
            holder.append(lines[i])
    r = chunks(holder, 19)
    
for i in range(0,len(r)):
    classlist.append(Information(r[i][0],r[i][1],r[i][2],r[i][3],r[i][4],r[i][5],r[i][6],r[i][7], r[i][8], r[i][9],
                     r[i][10], r[i][11], r[i][12], r[i][13], r[i][14], r[i][15], r[i][16], r[i][17], r[i][18]))
bubblesort(classlist)    

writingfile('r.html') 
classlist = []
r =[]
with open("s.txt", 'r', encoding = 'utf-8') as file:
    lines = file.readlines()
    holder = []
    counter = 0
    for i in range(0,len(lines)):
        lines[i] = lines[i][:-1]           
    for i in range(0,len(lines)):
            holder.append(lines[i])
    s = chunks(holder, 19)
    
for i in range(0,len(s)):
    classlist.append(Information(s[i][0],s[i][1],s[i][2],s[i][3],s[i][4],s[i][5],s[i][6],s[i][7], s[i][8], s[i][9],
                     s[i][10], s[i][11], s[i][12], s[i][13], s[i][14], s[i][15], s[i][16], s[i][17], s[i][18]))
bubblesort(classlist)    

writingfile('s.html') 
classlist = []
s =[]
with open("t.txt", 'r', encoding = 'utf-8') as file:
    lines = file.readlines()
    holder = []
    counter = 0
    for i in range(0,len(lines)):
        lines[i] = lines[i][:-1]           
    for i in range(0,len(lines)):
            holder.append(lines[i])
    t = chunks(holder, 19)
    
for i in range(0,len(t)):
    classlist.append(Information(t[i][0],t[i][1],t[i][2],t[i][3],t[i][4],t[i][5],t[i][6],t[i][7], t[i][8], t[i][9],
                     t[i][10], t[i][11], t[i][12], t[i][13], t[i][14], t[i][15], t[i][16], t[i][17], t[i][18]))
bubblesort(classlist)    

writingfile('t.html') 
classlist = []
t =[]
with open("u.txt", 'r', encoding = 'utf-8') as file:
    lines = file.readlines()
    holder = []
    counter = 0
    for i in range(0,len(lines)):
        lines[i] = lines[i][:-1]           
    for i in range(0,len(lines)):
            holder.append(lines[i])
    u = chunks(holder, 19)
    
for i in range(0,len(u)):
    classlist.append(Information(u[i][0],u[i][1],u[i][2],u[i][3],u[i][4],u[i][5],u[i][6],u[i][7], u[i][8], u[i][9],
                     u[i][10], u[i][11], u[i][12], u[i][13], u[i][14], u[i][15], u[i][16], u[i][17], u[i][18]))
bubblesort(classlist)    

writingfile('u.html') 
classlist = []
u =[]
with open("v.txt", 'r', encoding = 'utf-8') as file:
    lines = file.readlines()
    holder = []
    counter = 0
    for i in range(0,len(lines)):
        lines[i] = lines[i][:-1]           
    for i in range(0,len(lines)):
            holder.append(lines[i])
    v = chunks(holder, 19)
    
for i in range(0,len(v)):
    classlist.append(Information(v[i][0],v[i][1],v[i][2],v[i][3],v[i][4],v[i][5],v[i][6],v[i][7], v[i][8], v[i][9],
                     v[i][10], v[i][11], v[i][12], v[i][13], v[i][14], v[i][15], v[i][16], v[i][17], v[i][18]))
bubblesort(classlist)    

writingfile('v.html') 
classlist = []
v =[]
with open("w.txt", 'r', encoding = 'utf-8') as file:
    lines = file.readlines()
    holder = []
    counter = 0
    for i in range(0,len(lines)):
        lines[i] = lines[i][:-1]           
    for i in range(0,len(lines)):
            holder.append(lines[i])
    w = chunks(holder, 19)
    
for i in range(0,len(w)):
    classlist.append(Information(w[i][0],w[i][1],w[i][2],w[i][3],w[i][4],w[i][5],w[i][6],w[i][7], w[i][8], w[i][9],
                     w[i][10], w[i][11], w[i][12], w[i][13], w[i][14], w[i][15], w[i][16], w[i][17], w[i][18]))
bubblesort(classlist)    

writingfile('w.html') 
classlist = []
w = []
with open("x.txt", 'r', encoding = 'utf-8') as file:
    lines = file.readlines()
    holder = []
    counter = 0
    for i in range(0,len(lines)):
        lines[i] = lines[i][:-1]           
    for i in range(0,len(lines)):
            holder.append(lines[i])
    x = chunks(holder, 19)
    
for i in range(0,len(x)):
    classlist.append(Information(x[i][0],x[i][1],x[i][2],x[i][3],x[i][4],x[i][5],x[i][6],x[i][7], x[i][8], x[i][9],
                     x[i][10], x[i][11], x[i][12], x[i][13], x[i][14], x[i][15], x[i][16], x[i][17], x[i][18]))
bubblesort(classlist)    

writingfile('x.html') 
classlist = []
x =[]
with open("y.txt", 'r', encoding = 'utf-8') as file:
    lines = file.readlines()
    holder = []
    counter = 0
    for i in range(0,len(lines)):
        lines[i] = lines[i][:-1]           
    for i in range(0,len(lines)):
            holder.append(lines[i])
    y = chunks(holder, 19)
    
for i in range(0,len(y)):
    classlist.append(Information(y[i][0],y[i][1],y[i][2],y[i][3],y[i][4],y[i][5],y[i][6],y[i][7], y[i][8], y[i][9],
                     y[i][10], y[i][11], y[i][12], y[i][13], y[i][14], y[i][15], y[i][16], y[i][17], y[i][18]))
bubblesort(classlist)    

writingfile('y.html') 
classlist = []
y =[]
with open("z.txt", 'r', encoding = 'utf-8') as file:
    lines = file.readlines()
    holder = []
    counter = 0
    for i in range(0,len(lines)):
        lines[i] = lines[i][:-1]           
    for i in range(0,len(lines)):
            holder.append(lines[i])
    z = chunks(holder, 19)
    
for i in range(0,len(z)):
    classlist.append(Information(z[i][0],z[i][1],z[i][2],z[i][3],z[i][4],z[i][5],z[i][6],z[i][7], z[i][8], z[i][9],
                     z[i][10], z[i][11], z[i][12], z[i][13], z[i][14], z[i][15], z[i][16], z[i][17], z[i][18]))
bubblesort(classlist)    

writingfile('z.html') 
classlist = []
z =[]
end = time.time()
elapsed = end - start
print('Time Taken: ' + str(elapsed))

end1 = time.time()
elapsed = end1 - start1

print('Total setup run-time: ' + str(elapsed))
