-- 코드를 입력하세요
SELECT price div 10000 * 10000 PRICE_GROUP,count(*) from product group by price div 10000 order by price