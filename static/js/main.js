var js_data = document.getElementById('data').getAttribute('d');
alert(js_data);

let myChart = document.getElementById('myChart').getContext('2d');

            let barChart = new Chart(myChart,{
                type:'line',
                data:{
                    labels:['Boston','Worcester','Springfield','Lowell','Cambridge','New Bedford'],
                    datasets:[{
                        label:'Population',
                        data:[
                            617594,
                            181045,
                            153060,
                            155132,
                            95230
                        ]
                    }]
                },
                options:{}
            });