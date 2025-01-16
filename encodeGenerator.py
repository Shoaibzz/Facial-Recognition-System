import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://real-time-attendance-b2327-default-rtdb.firebaseio.com/",
    'storageBucket':"real-time-attendance-b2327.appspot.com"
})

folderPath = 'Images'
PathList = os.listdir(folderPath)
#print(PathList)
imgList = []
studentId = []
for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    studentId.append(os.path.splitext(path)[0])    

    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(os.path.join(folderPath,path))

#print(len(imgList))
print(studentId)


def findEncoding(iamgeList):
    encodeList = []
    for img in iamgeList:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        #encode = face_recognition.face_encodings(img)

        #print(encode)
        encodeList.append(encode)
    return encodeList
print("Encoding Started...")
encodeListKnown = findEncoding(imgList)
#print(encodeListKnown)
encodeListKnownWithId = [encodeListKnown,studentId]
#print(encodeListKnownWithId)
print("Encoding Complete")

file = open("EncodeFile.p","wb")
pickle.dump(encodeListKnownWithId,file)
file.close()
print("File Saved")