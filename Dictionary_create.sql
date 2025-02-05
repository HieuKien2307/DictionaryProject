-- Tạo database
CREATE DATABASE DictionaryDB;
USE DictionaryDB;

-- Bảng quản lý người dùng
CREATE TABLE Users (
    user_id INT PRIMARY KEY IDENTITY(1,1),
    username NVARCHAR(50) UNIQUE NOT NULL,
    password NVARCHAR(50) NOT NULL,
    created_at DATETIME DEFAULT GETDATE()
);

-- Bảng quản lý từ điển
CREATE TABLE Words (
    word_id INT PRIMARY KEY IDENTITY(1,1),
    word NVARCHAR(100) NOT NULL UNIQUE,
    part_of_speech NVARCHAR(20),
    definition NVARCHAR(MAX) NOT NULL,
    example NVARCHAR(MAX),
    created_at DATETIME DEFAULT GETDATE()
);

-- Bảng liên kết từ điển của người dùng
CREATE TABLE UserDictionary (
    user_word_id INT PRIMARY KEY IDENTITY(1,1),
    user_id INT FOREIGN KEY REFERENCES Users(user_id) ON DELETE CASCADE,
    word_id INT FOREIGN KEY REFERENCES Words(word_id) ON DELETE CASCADE,
    custom_definition NVARCHAR(MAX),
    view_count INT DEFAULT 0,
    search_count INT DEFAULT 0,
    created_at DATETIME DEFAULT GETDATE()
);

-- Bảng lưu thống kê hoạt động
CREATE TABLE WordStats (
    stat_id INT PRIMARY KEY IDENTITY(1,1),
    word_id INT FOREIGN KEY REFERENCES Words(word_id) ON DELETE CASCADE,
    user_id INT FOREIGN KEY REFERENCES Users(user_id) ON DELETE CASCADE,
    action NVARCHAR(20),
    action_time DATETIME DEFAULT GETDATE()
);

-- Thêm dữ liệu ban đầu (nếu cần)
-- Tạo database và cấu trúc bảng đã có từ trước
USE DictionaryDB;

-- Xóa dữ liệu nếu đã tồn tại để làm sạch cho việc test
DELETE FROM UserDictionary;
DELETE FROM WordStats;
DELETE FROM Words;

-- Import dữ liệu mẫu cho bảng Words
INSERT INTO Words (word, part_of_speech, definition, example) VALUES
('able', 'a', '(usually followed by `to`) having the necessary means or skill or know-how or authority to do something', 'able to swim, she was able to program her computer, we were at last able to buy a car, able to get a grant for the project'),
('unable', 'a', '(usually followed by `to`) not having the necessary means or skill or know-how', 'unable to get to town without a car, unable to obtain funds'),
('abaxial', 'a', 'facing away from the axis of an organ or organism', 'the abaxial surface of a leaf is the underside or side facing away from the stem'),
('adaxial', 'a', 'nearest to or facing toward the axis of an organ or organism', 'the upper side of a leaf is known as the adaxial surface');

SELECT *
from Words
