# separate value by space
set datafile separator " "



# output to PDF
set terminal pngcairo size 1000,250 font "Helvetica" background rgb "white"
set output "average.png"

set xlabel 'millisekonds'
set xrange [0:2500]
set ytics nomirror
set y2tics
#set x2tics nomirror
set xtics 0,500, 2500
set ylabel 'amplitude'

# auto generate stats for the "data.txt" file to use later
stats "data.txt" using 1:2 name "stats" 

#stats "temperature.txt" using 1:2 name "stats2" 



# funktion returning how many data points we have processed
# capped to at least 1 and max 5
samples(x) = $0>4?5 : ($0+1)

# function to put current data point in back1, previous back1 value into back2, ets...
shift5(x)=(back5=back4, back4=back3, back3=back2, back2=back1, back1=x)

# function that calls shift above, than calculate avarage of all backX values (last 1-5 data points)
avg5(x)=(shift5(x), (back1+back2+back3+back4+back5)/samples($0))

# function to initialise values to 0 at start
init(x)=(back1=back2=back3=back4=back5=sum=0)

# actual plot (Note: Using stats, not the date file)
# adding rodata 
plot "data.txt" using 1:2 with points pointtype 1 pointsize 1 axis x1y1,  sum = init(0), \
    '' using ($1 - stats_min_x):(avg5($2)) with lines smooth csplines lc rgb '#aa7777' title 'puls' axis x1y1, "temperature.txt" using 1:2 with lines axis x1y2





#plot sum = init(0), \
#   '' using ($1 - stats_min_x):(avg5($2)) with lines smooth csplines lc rgb '#aa7777' title 'puls' axis x1y1, "temperature.txt" using 1:2 with lines axis x1y2
        






#'data.txt' using ($1 - stats_min_x):($2) with points pointtype 1 pointsize 0.2 \
#axes x1y1 title 'Data points', \

#axes x1y1 title '5'

# avg5(x)=(shift5(x),(back1+back2+back3+back4+back5)/samples($0))