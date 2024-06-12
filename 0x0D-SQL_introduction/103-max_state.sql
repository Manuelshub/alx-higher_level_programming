-- This script displays the max temperature of each stateeee
SELECT `state`, MAX(`value`) AS max_temp
FROM temperatures
GROUP BY `state`
ORDER BY `state` ASC
