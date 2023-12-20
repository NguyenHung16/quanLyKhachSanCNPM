from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.orm import relationship, backref
from flask_login import UserMixin
from datetime import datetime
from app import db, app

class TaiKhoanNhanVien(db.Model, UserMixin):
    emp_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    active = Column(Boolean, default=True)
    taiKhoanAdmin = relationship('TaiKhoanAdmin', backref='TaiKhoanNhanVien', lazy=True)

    def __str__(self):
        return self.name

    def get_id(self):
        return self.emp_id

    def is_active(self):
        return self.active

    def activate_user(self):
        self.active = True

    def get_username(self):
        return self.username

    def get_urole(self):
        return 'NhanVien'


class TaiKhoanAdmin(db.Model):
    admin_id = Column(Integer, primary_key=True, autoincrement=True)
    emp_id = Column(Integer, ForeignKey(TaiKhoanNhanVien.emp_id), nullable=False)

    def __str__(self):
        return str(self.admin_id)


class LoaiPhong(db.Model):
    maLoaiPhong = Column(Integer, primary_key=True, autoincrement=True)
    loaiPhong = Column(String(5), nullable=False)
    donGia = Column(Integer, nullable=False)
    phong = relationship('Phong', backref='LoaiPhong', lazy=True)
class Phong(db.Model):
    maPhong = Column(Integer, primary_key=True, autoincrement=True)
    maLoaiPhong = Column(Integer, ForeignKey(LoaiPhong.maLoaiPhong), nullable=False)
    ghiChu = Column(String(255), nullable=True)
    tinhTrang = Column(String(2), nullable=False)
    hinhAnh = Column(String(255), nullable=True)
    chiTietThue = relationship('ChiTietThue', backref='phong_chiTietThue', lazy=True)
    danhGia = relationship('DanhGiaCuaKhach', backref='phong_danhGia', lazy=True)

    def __str__(self):
        return str(self.maPhong)


class LoaiKhach(db.Model):
    maLoaiKhach = Column(Integer, primary_key=True, autoincrement=True)
    loaiKhach = Column(String(50), nullable=False)
    khach = relationship('Khach', backref='LoaiKhach', lazy=True)


class Khach(db.Model):
    maKhach = Column(Integer, primary_key=True, autoincrement=True)
    maLoaiKhach = Column(Integer, ForeignKey(LoaiKhach.maLoaiKhach), nullable=False)
    CMND = Column(String(12), nullable=False)
    diaChi = Column(String(255), nullable=False)
    ngaySinh = Column(DateTime, nullable=True)
    chiTietThue = relationship('ChiTietThue', backref='Khach_ChiTietThue', lazy=True)
    danhGia = relationship('DanhGiaCuaKhach', backref='Khach_danhGia', lazy=True)
    taiKhoan = relationship('TaiKhoanKhach', backref='Khach_TaiKhoan', lazy=True, )

    def __str__(self):
        return str(self.maKhach)


class TaiKhoanKhach(db.Model):
    maKhach = Column(Integer, ForeignKey(Khach.maKhach), primary_key=True, nullable=False)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)

    def get_id(self):
        return self.maKhach

    def is_active(self):
        return True

    def get_username(self):
        return self.username

    def get_urole(self):
        return 'Khach'



class ChiTietThue(db.Model):
    maHopDong = Column(Integer, primary_key=True, autoincrement=True)
    maPhong = Column(Integer, ForeignKey(Phong.maPhong), nullable=False)
    maKhach = Column(Integer, ForeignKey(Khach.maKhach), nullable=False)
    ngayBatDau = Column(DateTime, default=datetime.now(), nullable=False)
    soNgayODuKien = Column(Integer, nullable=True)

    hopDong = relationship('HoaDon', backref='ChiTietThue', lazy=True)

    def __str__(self):
        return str(self.maHopDong)


class DanhGiaCuaKhach(db.Model):
    maDanhGia = Column(Integer, primary_key=True, autoincrement=True)
    maPhong = Column(Integer, ForeignKey(Phong.maPhong), nullable=False)
    maKhach = Column(Integer, ForeignKey(Khach.maKhach), nullable=False)
    ngayBatDau = Column(DateTime, default=datetime.now(), nullable=False)
    noiDung = Column(String(255), nullable=False)
    soSao = Column(Integer, nullable=True)

    def __str__(self):
        return str(self.maDanhGia)


class HoaDon(db.Model):
    maHopDong = Column(Integer, ForeignKey(ChiTietThue.maHopDong), primary_key=True)
    ngayTraPhong = Column(DateTime, default=datetime.now(), nullable=False)
    thanhTien = Column(Integer, nullable=False)

    def __str__(self):
        return str(self.maHopDong)


class ThongSoQuyDinh(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    loai = Column(String(50), nullable=False)
    giaTri = Column(Float, nullable=False)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
