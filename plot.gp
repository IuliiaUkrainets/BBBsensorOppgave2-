set output 'plot.pdf'
set terminal pdf background rgb 'white'
set datafile separator ' '



set xlabel 'millisekonds'
set xtics 10 rotate by 50 offset 0, -10 out 
set ylabel 'amplitude'
stats 'data.txt' using 1:2 name "stats"

set  xdata  time 
set  timefmt "%s"
set  format x "%S"


set autoscale y
set autoscale y2
set ytics nomirror





samples(x)=$0>4?5:($0+1)
avg5(x)=(shift5(x),(back1+back2+back3+back4+back5)/samples($0))
shift5(x)=(back5=back4,back4=back3,back3=back2,back2=back1,back1=x)
init(x)=(back1=back2=back3=back4=back5=sum=0)

plot sum = init(0), \
'data.txt' using ($1 - stats_min_x):($2) with points pointtype 1 pointsize 0.2 \
axes x1y1 title 'Data points', \
'' using ($1 - stats_min_x):(avg5($2)) with lines smooth csplines \
   axes x1y1 title '5 Data points'
