SELECT regname AS REGION, year as YEAR, AVG(engball100) as ENG_AVERAGE_MARK
FROM ZNO_STATS
WHERE engteststatus = 'Зараховано'
GROUP BY regname, year
ORDER BY ENG_AVERAGE_MARK DESC;
