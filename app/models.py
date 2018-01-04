from app import db

class Base(db.Model):
    '''
    Base defines the common fields in all the models
    '''
    __abstract__ = True
    code = db.Column(db.Integer, db.Sequence('seq_reg_id', start=1, increment=1), primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
        return self
    
    def get_one(self, code):
        return self.query.filter_by(code=code).first()
    
    def get_all(self):
        return self.query.order_by(self.code).all()


class County(Base):
    '''
    County defines the underlying fields of a county model
    '''

    def __repr__(self):
        return "<County code:%r name:%r" % (self.code, self.name)

class Constituency(Base):
    '''
    Constituency defines the underlying fields of a constituency model
    '''
    county_code = db.Column(db.Integer, db.ForeignKey("county.code"))

    def get_by_county_code(self, code):
        return self.query.order_by(Constituency.code).filter_by(county_code=code).all()

    def __repr__(self):
        return "<Constituency code:%r name:%r county_code:%r" % (
            self.code, self.name, self.county_code)

class Ward(Base):
    '''
    Ward defines the underlying fields of a Ward model.
    '''
    constituency_code = db.Column(db.Integer, db.ForeignKey("constituency.code"))

    def get_by_constituency_code(self, code):
        return self.query.order_by(Ward.code).filter_by(constituency_code=code).all()

    def __repr__(self):
        return "<Ward code:%r name:%r constituency_code:%r" % (
            self.code, self.name, self.constituency_code)