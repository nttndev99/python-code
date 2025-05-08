
from datetime import datetime
from app.models.post import Posts
from app.models.user import Users
from app.extensions import db

def seed_data():
    current_time = datetime.now()
    time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
    
    has_users = Users.query.first() is not None
    has_posts = Posts.query.first() is not None
    
    try:
        if not has_users and not has_posts:
            user = Users(
                id=1,
                name='Admin',
                email='admin@email.com',
                password='pbkdf2:sha256:1000000$j73phBAC$46592241d998f37088bb32bcd524dc49726d5d659bab21f911d6adf2c00cb296')
            post1 = Posts(
                id = 1,
                title='The Life of Cactus',
                subtitle='Who knew that cacti lived such interesting lives.',
                date= time_str,
                img_url='img_post1',
                body='Nori grape silver beet broccoli kombu beet greens fava bean potato quandong celery. Bunya nuts black-eyed pea prairie turnip leek lentil turnip greens parsnip. Sea lettuce lettuce water chestnut eggplant winter purslane fennel azuki bean earthnut pea sierra leone bologi leek soko chicory celtuce parsley jícama salsify.',
                author=user)  
            post2 = Posts(
                id = 2,
                title='Top 15 Things to do When You are Bored',
                subtitle='Are you bored? Don\'t know what to do? Try these top 15 activities.',
                date= time_str,
                img_url='img_post2',
                body='Chase ball of string eat plants, meow, and throw up because I ate plants going to catch the red dot today going to catch the red dot today. I could pee on this if I had the energy. Chew iPad power cord steal the warm chair right after you get up for purr for no reason leave hair everywhere, decide to want nothing to do with my owner today.',
                author=user)        
            post3 = Posts(
                id = 3,
                title='Introduction to Intermittent Fasting',
                subtitle='Learn about the newest health craze.',
                date= time_str,
                img_url='img_post3',
                body='Cupcake ipsum dolor. Sit amet marshmallow topping cheesecake muffin. Halvah croissant candy canes bonbon candy. Apple pie jelly beans topping carrot cake danish tart cake cheesecake. Muffin danish chocolate soufflé pastry icing bonbon oat cake. Powder cake jujubes oat cake. Lemon drops tootsie roll marshmallow halvah carrot cake.',
                author=user)
            db.session.add_all([user, post1, post2, post3])
            db.session.commit()
            print("✅ Seed data created successfully!")
        else:
            print("ℹ️ Seed data already exists.")
    except Exception as e:
        print(f"❌ Error seeding data: {e}")