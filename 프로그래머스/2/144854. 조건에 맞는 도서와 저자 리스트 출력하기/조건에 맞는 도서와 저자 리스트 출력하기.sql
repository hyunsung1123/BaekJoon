-- 코드를 입력하세요
SELECT BOOK_ID, AUTHOR_NAME, DATE_FORMAT(PUBLISHED_DATE,'%Y-%m-%d') FROM BOOK B NATURAL JOIN AUTHOR A WHERE CATEGORY = '경제' ORDER BY PUBLISHED_DATE;  