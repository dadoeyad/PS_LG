var items = {};

function sum(values) {
    return _.reduce(values, function(memo, num){ return memo + num; }, 0);
}
$.getJSON(json_url, function( data ) {
      items = data;
      cat1_values = _.pluck(_.where(items, {cat: "CAT 1"}), 'value');
      cat2_values = _.pluck(_.where(items, {cat: "CAT 2"}), 'value');
      cat3_values = _.pluck(_.where(items, {cat: "CAT 3"}), 'value');
      cat4_values = _.pluck(_.where(items, {cat: "CAT 4"}), 'value');

      all_values = _.pluck(items, 'value');
      sum_values = sum(all_values)

      cat1_percent = sum(cat1_values) / sum_values * 100;
      cat2_percent = sum(cat2_values) / sum_values * 100;
      cat3_percent = sum(cat3_values) / sum_values * 100;
      cat4_percent = sum(cat4_values) / sum_values * 100;

      $('#line').highcharts({
        title: {
            text: 'Categories values',
            x: -20 //center
        },
        xAxis: {
            categories: _(items).chain().flatten().pluck('date').unique().value()
        },
        yAxis: {
            title: {
                text: 'values'
            },
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0
        },
        series: [{
            name: 'CAT 1',
            data: cat1_values
        }, {
            name: 'CAT 2',
            data: cat2_values
        }, {
            name: 'CAT 3',
            data: cat3_values
        }, {
            name: 'CAT 4',
            data: cat4_values
        }]
    });


    $('#pie').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie'
        },
        title: {
            text: 'test'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                    style: {
                        color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                    }
                }
            }
        },
        series: [{
            name: 'Brands',
            colorByPoint: true,
            data: [{
                name: 'CAT 1',
                y: cat1_percent
            }, {
                name: 'CAT 2',
                y: cat2_percent,
                sliced: true,
                selected: true
            }, {
                name: 'CAT 3',
                y: cat3_percent
            }, {
                name: 'CAT 4',
                y: cat4_percent
            }]
        }]
    });
});