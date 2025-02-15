# lincride-project


### Setup
1. Clone the repository
```bash
git clone https://github.com/iyanuashiri/lincride-assessment.git
cd lincride-assessment
```

2. Enter the linride-backend 
```bash
cd lincride-backend

```

3. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```


4. Install dependencies
```bash
pip install -r requirements.txt
```

5. Run migrations
```bash
python manage.py migrate
```

6. Run tests
```bash
python manage.py test lincride/rides/tests/

python manage.py test lincride/rides/tests/ -v 2

```


Visit `http://localhost:8000/api/v1/calculate-fare/?distance=5&traffic_level=low&demand_level=normal` in your postman.


1. I added the Ride data model for audit reasons. 
2. There would probably been a driver and a rider fields, but because of the specific tasks in the project, I didnt use them. Included them because I think they would have been needed in real life(production) 