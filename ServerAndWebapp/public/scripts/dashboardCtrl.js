function convertDate(inputFormat) {
	var d = new Date(inputFormat);
	return [d.getHours(), d.getMinutes(), d.getSeconds()].join(':');
 }

function updateData() {

	$.ajax({
		url: 'http://'+window.location.hostname+'/api/data',
		success: function(data) {
			refreshData(data.data);
		},
	});
}

function refreshData(data_in) {

	var data = { "exth1" : [], "exth2" : [], "h1" : [], "h2" : [], "extt1" : [], "extt2" : [], "t1" : [], "t2" : [], "light" : [], "timestamp" : []};

	for(var i = 0; i < data_in.length; ++i) {

		data["exth1"][i] = [i, data_in[i]["exth1"]];
		data["exth2"][i] = [i, data_in[i]["exth2"]];
		data["h1"][i] = [i, data_in[i]["h1"]];
		data["h2"][i] = [i, data_in[i]["h2"]];
		data["extt1"][i] = [i, data_in[i]["extt1"]];
		data["extt2"][i] = [i, data_in[i]["extt2"]];
		data["t1"][i] = [i, data_in[i]["t1"]];
		data["t2"][i] = [i, data_in[i]["t2"]];
		data["light"][i] = [i, data_in[i]["light"]];

		data["timestamp"][i] = i;
	}

	$.plot($("#ext-humidity-chart1"),
		[{
			data : data["exth1"],
			label : "Exterior humidity 1",
			color: "#0a3683"
		}],
		{
			series: {
				lines : {
					show : true,
					fill : true,
					lineWidth : 2,
					fillColor : {
						colors : [{
							opacity : 0.05
						}, {
							opacity : 0.05
						}]
					}
				},
				points: {
					show: false
				},
				shadowSize : 0
			},
			grid : {
				hoverable : true,
				clickable : true,
				borderColor : "#f9f9f9",
				tickColor : "#AAAAAA",
				borderWidth : 1,
				labelMargin : 10,
				backgroundColor : "#fff"
			},
			legend : {
				position : "ne",
				margin : [0, -24],
				noColumns : 0,
				labelBoxBorderColor : null,
				labelFormatter : function(label, series) {
					// just add some space to labes
					return '' + label + '&nbsp;&nbsp;';
				},
				width : 30,
				height : 2
			},
			yaxis : {
				tickColor : '#f5f5f5',
				tickDecimals: 0,
				font : {
					color : '#bdbdbd'
				}
			},
			xaxis : {
				tickColor : '#f5f5f5',
				ticks: data["timestamp"],
				rotateTicks: 45,
				font : {
					color : '#bdbdbd'
				}
			},
			tooltip : true,
			tooltipOpts : {
				content : '%s: %y',
				shifts : {
					x : -60,
					y : 25
				},
				defaultTheme : false
			}
		}
	);

	$.plot($("#ext-humidity-chart2"),
		[{
			data : data["exth2"],
			label : "Exterior humidity 2",
			color: "#0a3683"
		}],
		{
			series: {
				lines : {
					show : true,
					fill : true,
					lineWidth : 2,
					fillColor : {
						colors : [{
							opacity : 0.05
						}, {
							opacity : 0.05
						}]
					}
				},
				points: {
					show: false
				},
				shadowSize : 0
			},
			grid : {
				hoverable : true,
				clickable : true,
				borderColor : "#f9f9f9",
				tickColor : "#AAAAAA",
				borderWidth : 1,
				labelMargin : 10,
				backgroundColor : "#fff"
			},
			legend : {
				position : "ne",
				margin : [0, -24],
				noColumns : 0,
				labelBoxBorderColor : null,
				labelFormatter : function(label, series) {
					// just add some space to labes
					return '' + label + '&nbsp;&nbsp;';
				},
				width : 30,
				height : 2
			},
			yaxis : {
				tickColor : '#f5f5f5',
				tickDecimals: 0,
				font : {
					color : '#bdbdbd'
				}
			},
			xaxis : {
				tickColor : '#f5f5f5',
				ticks: data["timestamp"],
				rotateTicks: 45,
				font : {
					color : '#bdbdbd'
				}
			},
			tooltip : true,
			tooltipOpts : {
				content : '%s: %y',
				shifts : {
					x : -60,
					y : 25
				},
				defaultTheme : false
			}
		});

		$.plot($("#int-humidity-chart1"), [{
		data : data["h1"],
		label : "Humidity 1",
		color: "#0a3683"
		}], {
		series: {
		  lines : {
				show : true,
				fill : true,
				lineWidth : 2,
				fillColor : {
				    colors : [{
				        opacity : 0.05
				    }, {
				        opacity : 0.05
				    }]
				}
		        },
		  points: {
		    show: false
		  },
		  shadowSize : 0
		},
		grid : {
		        hoverable : true,
		        clickable : true,
		        borderColor : "#f9f9f9",
		        tickColor : "#AAAAAA",
		        borderWidth : 1,
		        labelMargin : 10,
		        backgroundColor : "#fff"
		    },
		legend : {
		        position : "ne",
		        margin : [0, -24],
		        noColumns : 0,
		        labelBoxBorderColor : null,
		        labelFormatter : function(label, series) {
				// just add some space to labes
				return '' + label + '&nbsp;&nbsp;';
		        },
		        width : 30,
		        height : 2
		    },
		yaxis : {
		        tickColor : '#f5f5f5',
		  tickDecimals: 0,
		        font : {
				color : '#bdbdbd'
		        }
		    },
		    xaxis : {
		        tickColor : '#f5f5f5',
		  ticks: data["timestamp"],
		  rotateTicks: 45,
		        font : {
				color : '#bdbdbd'
		        }
		    },
		    tooltip : true,
		    tooltipOpts : {
		        content : '%s: %y',
		        shifts : {
				x : -60,
				y : 25
		        },
		        defaultTheme : false
		    }
		});
		$.plot($("#int-humidity-chart2"), [{
		data : data["h2"],
		label : "Humidity 2",
		color: "#0a3683"
		}], {
		series: {
		  lines : {
				show : true,
				fill : true,
				lineWidth : 2,
				fillColor : {
				    colors : [{
				        opacity : 0.05
				    }, {
				        opacity : 0.05
				    }]
				}
		        },
		  points: {
		    show: false
		  },
		  shadowSize : 0
		},
		grid : {
		        hoverable : true,
		        clickable : true,
		        borderColor : "#f9f9f9",
		        tickColor : "#AAAAAA",
		        borderWidth : 1,
		        labelMargin : 10,
		        backgroundColor : "#fff"
		    },
		legend : {
		        position : "ne",
		        margin : [0, -24],
		        noColumns : 0,
		        labelBoxBorderColor : null,
		        labelFormatter : function(label, series) {
				// just add some space to labes
				return '' + label + '&nbsp;&nbsp;';
		        },
		        width : 30,
		        height : 2
		    },
		yaxis : {
		        tickColor : '#f5f5f5',
		  tickDecimals: 0,
		        font : {
				color : '#bdbdbd'
		        }
		    },
		    xaxis : {
		        tickColor : '#f5f5f5',
		  ticks: data["timestamp"],
		  rotateTicks: 45,
		        font : {
				color : '#bdbdbd'
		        }
		    },
		    tooltip : true,
		    tooltipOpts : {
		        content : '%s: %y',
		        shifts : {
				x : -60,
				y : 25
		        },
		        defaultTheme : false
		    }
		});
		$.plot($("#ext-temperature-chart1"), [{
		data : data["extt1"],
		label : "Exterior temperature 1",
		color: "#CF482E"
		}], {
		series: {
		  lines : {
				show : true,
				fill : true,
				lineWidth : 2,
				fillColor : {
				    colors : [{
				        opacity : 0.05
				    }, {
				        opacity : 0.05
				    }]
				}
		        },
		  points: {
		    show: false
		  },
		  shadowSize : 0
		},
		grid : {
		        hoverable : true,
		        clickable : true,
		        borderColor : "#f9f9f9",
		        tickColor : "#AAAAAA",
		        borderWidth : 1,
		        labelMargin : 10,
		        backgroundColor : "#fff"
		    },
		legend : {
		        position : "ne",
		        margin : [0, -24],
		        noColumns : 0,
		        labelBoxBorderColor : null,
		        labelFormatter : function(label, series) {
				// just add some space to labes
				return '' + label + '&nbsp;&nbsp;';
		        },
		        width : 30,
		        height : 2
		    },
		yaxis : {
		        tickColor : '#f5f5f5',
		  tickDecimals: 0,
		        font : {
				color : '#bdbdbd'
		        }
		    },
		    xaxis : {
		        tickColor : '#f5f5f5',
		  ticks: data["timestamp"],
		  rotateTicks: 45,
		        font : {
				color : '#bdbdbd'
		        }
		    },
		    tooltip : true,
		    tooltipOpts : {
		        content : '%s: %y',
		        shifts : {
				x : -60,
				y : 25
		        },
		        defaultTheme : false
		    }
		});
		$.plot($("#ext-temperature-chart2"), [{
		data : data["extt2"],
		label : "Exterior temperature 2",
		color: "#CF482E"
		}], {
		series: {
		  lines : {
				show : true,
				fill : true,
				lineWidth : 2,
				fillColor : {
				    colors : [{
				        opacity : 0.05
				    }, {
				        opacity : 0.05
				    }]
				}
		        },
		  points: {
		    show: false
		  },
		  shadowSize : 0
		},
		grid : {
		        hoverable : true,
		        clickable : true,
		        borderColor : "#f9f9f9",
		        tickColor : "#AAAAAA",
		        borderWidth : 1,
		        labelMargin : 10,
		        backgroundColor : "#fff"
		    },
		legend : {
		        position : "ne",
		        margin : [0, -24],
		        noColumns : 0,
		        labelBoxBorderColor : null,
		        labelFormatter : function(label, series) {
				// just add some space to labes
				return '' + label + '&nbsp;&nbsp;';
		        },
		        width : 30,
		        height : 2
		    },
		yaxis : {
		        tickColor : '#f5f5f5',
		  tickDecimals: 0,
		        font : {
				color : '#bdbdbd'
		        }
		    },
		    xaxis : {
		        tickColor : '#f5f5f5',
				ticks: data["timestamp"],
		  rotateTicks: 45,
		        font : {
				color : '#bdbdbd'
		        }
		    },
		    tooltip : true,
		    tooltipOpts : {
		        content : '%s: %y',
		        shifts : {
				x : -60,
				y : 25
		        },
		        defaultTheme : false
		    }
		});
		$.plot($("#int-temperature-chart1"), [{
		data : data["t1"],
		label : "Temperature 1",
		color: "#CF482E"
		}], {
		series: {
		  lines : {
				show : true,
				fill : true,
				lineWidth : 2,
				fillColor : {
				    colors : [{
				        opacity : 0.05
				    }, {
				        opacity : 0.05
				    }]
				}
		        },
		  points: {
		    show: false
		  },
		  shadowSize : 0
		},
		grid : {
		        hoverable : true,
		        clickable : true,
		        borderColor : "#f9f9f9",
		        tickColor : "#AAAAAA",
		        borderWidth : 1,
		        labelMargin : 10,
		        backgroundColor : "#fff"
		    },
		legend : {
		        position : "ne",
		        margin : [0, -24],
		        noColumns : 0,
		        labelBoxBorderColor : null,
		        labelFormatter : function(label, series) {
				// just add some space to labes
				return '' + label + '&nbsp;&nbsp;';
		        },
		        width : 30,
		        height : 2
		    },
		yaxis : {
		        tickColor : '#f5f5f5',
		  tickDecimals: 0,
		        font : {
				color : '#bdbdbd'
		        }
		    },
		    xaxis : {
		        tickColor : '#f5f5f5',
				ticks: data["timestamp"],
		  rotateTicks: 45,
		        font : {
				color : '#bdbdbd'
		        }
		    },
		    tooltip : true,
		    tooltipOpts : {
		        content : '%s: %y',
		        shifts : {
				x : -60,
				y : 25
		        },
		        defaultTheme : false
		    }
		});
		$.plot($("#int-temperature-chart2"), [{
		data : data["t2"],
		label : "Temperature 2",
		color: "#CF482E"
		}], {
		series: {
		  lines : {
				show : true,
				fill : true,
				lineWidth : 2,
				fillColor : {
				    colors : [{
				        opacity : 0.05
				    }, {
				        opacity : 0.05
				    }]
				}
		        },
		  points: {
		    show: false
		  },
		  shadowSize : 0
		},
		grid : {
		        hoverable : true,
		        clickable : true,
		        borderColor : "#f9f9f9",
		        tickColor : "#AAAAAA",
		        borderWidth : 1,
		        labelMargin : 10,
		        backgroundColor : "#fff"
		    },
		legend : {
		        position : "ne",
		        margin : [0, -24],
		        noColumns : 0,
		        labelBoxBorderColor : null,
		        labelFormatter : function(label, series) {
				// just add some space to labes
				return '' + label + '&nbsp;&nbsp;';
		        },
		        width : 30,
		        height : 2
		    },
		yaxis : {
		        tickColor : '#f5f5f5',
		  tickDecimals: 0,
		        font : {
				color : '#bdbdbd'
		        }
		    },
		    xaxis : {
		        tickColor : '#f5f5f5',
				ticks: data["timestamp"],
		  rotateTicks: 45,
		        font : {
				color : '#bdbdbd'
		        }
		    },
		    tooltip : true,
		    tooltipOpts : {
		        content : '%s: %y',
		        shifts : {
				x : -60,
				y : 25
		        },
		        defaultTheme : false
		    }
		});

	$.plot($("#light-chart"),
		[{
			data : data["light"],
			label : "Light",
			color: "#FFB41E"
		}],
		{
			series: {
				lines : {
					show : true,
					fill : true,
					lineWidth : 2,
					fillColor : {
						colors : [{
							opacity : 0.05
						}, {
							opacity : 0.05
						}]
					}
				},
				points: {
					show: false
				},
				shadowSize : 0
			},
			grid : {
				hoverable : true,
				clickable : true,
				borderColor : "#f9f9f9",
				tickColor : "#AAAAAA",
				borderWidth : 1,
				labelMargin : 10,
				backgroundColor : "#fff"
			},
			legend : {
				position : "ne",
				margin : [0, -24],
				noColumns : 0,
				labelBoxBorderColor : null,
				labelFormatter : function(label, series) {
					// just add some space to labes
					return '' + label + '&nbsp;&nbsp;';
				},
				width : 30,
				height : 2
			},
			yaxis : {
				tickColor : '#f5f5f5',
				tickDecimals: 0,
				font : {
					color : '#bdbdbd'
				}
			},
			xaxis : {
				tickColor : '#f5f5f5',
				ticks: data["timestamp"],
				rotateTicks: 45,
				font : {
					color : '#bdbdbd'
				}
			},
			tooltip : true,
			tooltipOpts : {
				content : '%s: %y',
				shifts : {
					x : -60,
					y : 25
				},
				defaultTheme : false
			}
		}
	);
}
