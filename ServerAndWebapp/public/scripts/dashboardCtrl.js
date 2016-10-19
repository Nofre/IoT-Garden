function convertDate(inputFormat) {
	var d = new Date(inputFormat);
	return [d.getHours(), d.getMinutes(), d.getSeconds()].join(':');
 }

function updateData() {

	for(var i = 0; i < data.length; ++i) {
		var samples = [];
		var dataY = [];

		for(var j in data[i].samples) {
			samples.push([j, data[i].samples[j].value]);
			var aux = convertDate(data[i].samples[j].date);
			dataY.push([j, j]);
		}

		data[i].samples = samples;
		data[i].dates = dataY;
	}

	$.plot($("#ext-humidity-chart1"),
		[{
			data : data[0].samples,
			label : data[0].name,
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
				ticks: data[0].dates,
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
			data : data[1].samples,
			label : data[1].name,
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
		  ticks: data[0].dates,
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
		data : data[2].samples,
		label : data[2].name,
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
		  ticks: data[0].dates,
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
		data : data[3].samples,
		label : data[3].name,
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
		  ticks: data[0].dates,
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
		data : data[4].samples,
		label : data[4].name,
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
		  ticks: data[0].dates,
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
		data : data[5].samples,
		label : data[5].name,
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
		  ticks: data[0].dates,
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
		data : data[6].samples,
		label : data[6].name,
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
		  ticks: data[0].dates,
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
		data : data[7].samples,
		label : data[7].name,
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
		  ticks: data[0].dates,
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
			data : data[8].samples,
			label : data[8].name,
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
				ticks: data[0].dates,
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
