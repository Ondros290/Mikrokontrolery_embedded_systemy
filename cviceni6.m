
data = readmatrix("ntc.csv");

temp = data(:,1);
adc = data(:,2);

adc_value = (adc./(10+adc)) * (1023);
%adc_value = adc_value(:,1);

figure
plot(adc_value, temp)
xlabel('adc value');
ylabel('temperature');

% Set custom axis ranges
axis([0 1200 -50 200]);  % [xmin xmax ymin ymax]

p = polyfit(adc_value,temp,10);

ad2 = 0:1023;

t2 = round(polyval(p, ad2), 1);
hold on, plot(ad2, t2, 'r');

dlmwrite('data.dlm', t2*10, ',');



