from flask import Flask, render_template

app = Flask(__name__)

# Sample data for cars with purchase links
cars =[
    {
        "id": 1,
        "name": "Pininfarina Battista",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQ3B1Msd1tBNUPq7seP3WZuOV-tYHuBi20hjJ_mxKGsEnLnhk4VzGqp2Lj3A2ZYCdEeog&usqp=CAU",
        "price": "$80,000",
        "type": "Electric",
        "purchase_link": "https://www.pininfarina.it"
    },
    {
        "id": 2,
        "name": "Ford Mustang",
        "image": "https://i.insider.com/5e9a0cafdcd88c113f7c08b0?width=700",
        "price": "$55,000",
        "type": "Sports",
        "purchase_link": "https://www.ford.com"
    },
    {
        "id": 3,
        "name": "Aston Martin DB12",
        "image": "https://hips.hearstapps.com/hmg-prod/images/2024-aston-martin-db12-106-64933a95917aa.jpg?crop=0.668xw:0.563xh;0.0962xw,0.327xh&resize=2048:*",
        "price": "$25,000",
        "type": "Sedan",
        "purchase_link": "https://www.astonmartin.com"
    },
    {
        "id": 4,
        "name": "BMW X5",
        "image": "https://www.usnews.com/object/image/00000191-25b6-d8d6-a3fb-f5f6b8c60001/01-usnpx-2025bmwx5-angularfront-jmv.JPG?update-time=1722914668697&size=responsiveGallery",
        "price": "$70,000",
        "type": "SUV",
        "purchase_link": "https://www.bmw.com"
    },
    {
        "id": 5,
        "name": "Land Rover Defender",
        "image": "https://inkasarmored.com/wp-content/uploads/INKAS-Land-Rover-2023-Defender-1.jpg",
        "price": "$80,000",
        "type": "Electric",
        "purchase_link": "https://www.pininfarina.it"
    },
    {
        "id": 6,
        "name": "Porsche 918 spyder",
        "image": "https://robbreport.com/wp-content/uploads/2021/07/1-15.jpg",
        "price": "$80,000",
        "type": "Electric",
        "purchase_link": "https://www.pininfarina.it"
    },
]

bikes = [
    {
        "id": 1,
        "name": "Ducati Panigale V4",
        "image": "https://www.roadracingworld.com/wp-content/uploads/2022/07/DUCATI_PANIGALE_V4S_STATIC_001_UC355519_High_1657552868-e1657552884731.jpg",
        "price": "$40,000",
        "type": "Superbike",
        "purchase_link": "https://www.ducati.com"
    },
    {
        "id": 2,
        "name": "Yamaha R1",
        "image": "https://www.rushlane.com/wp-content/uploads/2024/02/yamaha-r1-discontinued-4.jpg",
        "price": "$25,000",
        "type": "Sports",
        "purchase_link": "https://www.yamaha-motor.com"
    },
    {
        "id": 3,
        "name": "Suzuki Hayabusa",
        "image": "https://cdpcdn.dx1app.com/products/USA/SU/2025/MC/SUPERSPORT/HAYABUSA/50/METALLIC_MYSTIC_SILVER_-_PEARL_VIGOR_BLUE/2000000001.jpg",
        "price": "$22,000",
        "type": "Hyperbike",
        "purchase_link": "https://www.suzukicycles.com"
    },
    {
        "id": 4,
        "name": "Honda CBR 1000RR",
        "image": "https://www.motorcyclenews.com/wp-images/4952/honda_fireblade_01.jpg",
        "price": "$28,000",
        "type": "Superbike",
        "purchase_link": "https://powersports.honda.com"
    },
    {
        "id": 5,
        "name": "Royal Enfield Meteor 350",
        "image": "https://stat.overdrive.in/wp-content/uploads/2023/10/2023-RE-Meteor-350-4-900x506.jpg",
        "price": "$5,000",
        "type": "Cruiser",
        "purchase_link": "https://www.royalenfield.com"
    },
    {
        "id": 6,
        "name": "BMW S1000RR",
        "image": "https://images.unsplash.com/photo-1635073943212-f34dfbfcc3b0?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Ym13JTIwczEwMDBycnxlbnwwfHwwfHx8MA%3D%3D",
        "price": "$32,000",
        "type": "Superbike",
        "purchase_link": "https://www.bmwmotorcycles.com"
    }
]

@app.route('/bikes')
def bikes_page():
    return render_template('bikes.html', bikes=bikes)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/cars')
def cars_page():
    return render_template('cars.html', cars=cars)

@app.route('/contact')
def contact_page():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
