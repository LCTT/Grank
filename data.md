<script src="https://cdn.jsdelivr.net/npm/echarts@4.6.0/dist/echarts.min.js" integrity="sha256-9TvhGliyfFW2O8SvloAhdFQbfjluHQ+vQ7WWWX5Z7oM=" crossorigin="anonymous"></script>

# 数据

## 分析方案

由于软件开发项目的迭代周期、研发难度有所不同，放在一个榜单内评比对于各项目来说，略显不公，因此，2019 年的 Grank 报告我们将参与分析的开源项目切分为以下四个类目，开源项目在同一类目下进行对比，具体分为以下四个类目：

1. **大前端类**：包括 iOS、Android、Web 大前端，主要为 Library
2. **服务端类**：包括 Java、Rust、PHP，主要为常见业务后台 Library 、Middleware
3. **工程类**：不限制语言，主要为可直接交付给C 端客户使用的项目，不作为开发工具参与到开发流程中。
4. **文档类**：主要是各类型的文档项目。
5. **物联网类**：面向物联网场景下的服务端应用、操作系统等应用。
6. **其他类**：无法被涵盖在上述分类范围的项目


## 大前端类分析结果
### 榜单情况

### 项目点评
#### [项目1](#)

<div id="project1" style="width: 100%;height:400px;"></div>
<script type="text/javascript">
// 基于准备好的dom，初始化echarts实例
var myChart = echarts.init(document.getElementById('project1'));

// 指定图表的配置项和数据
var option = {
    title: {
        text: 'XXX项目活跃度数据'
    },
    tooltip: {},
    legend: {
        data:['日期']
    },
    xAxis: {
        data: ["2017-01","2017-02","2017-03","2017-04","2017-05","2017-06"]
    },
    yAxis: {},
    series: [{
        name: '活跃度',
        type: 'line',
        data: [5, 20, 36, 10, 10, 20]
    }]
};

// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);
</script>

## 项目汇总

#### [项目2](#)

<div id="project2" style="width: 100%;height:400px;"></div>
<script type="text/javascript">
// 基于准备好的dom，初始化echarts实例
var myChart = echarts.init(document.getElementById('project2'));

// 指定图表的配置项和数据
var data = [
    [[28604,77,17096869,'Australia',1990],[31163,77.4,27662440,'Canada',1990],[1516,68,1154605773,'China',1990],[13670,74.7,10582082,'Cuba',1990],[28599,75,4986705,'Finland',1990],[29476,77.1,56943299,'France',1990],[31476,75.4,78958237,'Germany',1990],[28666,78.1,254830,'Iceland',1990],[1777,57.7,870601776,'India',1990],[29550,79.1,122249285,'Japan',1990],[2076,67.9,20194354,'North Korea',1990],[12087,72,42972254,'South Korea',1990],[24021,75.4,3397534,'New Zealand',1990],[43296,76.8,4240375,'Norway',1990],[10088,70.8,38195258,'Poland',1990],[19349,69.6,147568552,'Russia',1990],[10670,67.3,53994605,'Turkey',1990],[26424,75.7,57110117,'United Kingdom',1990],[37062,75.4,252847810,'United States',1990]],
    [[44056,81.8,23968973,'Australia',2015],[43294,81.7,35939927,'Canada',2015],[13334,76.9,1376048943,'China',2015],[21291,78.5,11389562,'Cuba',2015],[38923,80.8,5503457,'Finland',2015],[37599,81.9,64395345,'France',2015],[44053,81.1,80688545,'Germany',2015],[42182,82.8,329425,'Iceland',2015],[5903,66.8,1311050527,'India',2015],[36162,83.5,126573481,'Japan',2015],[1390,71.4,25155317,'North Korea',2015],[34644,80.7,50293439,'South Korea',2015],[34186,80.6,4528526,'New Zealand',2015],[64304,81.6,5210967,'Norway',2015],[24787,77.3,38611794,'Poland',2015],[23038,73.13,143456918,'Russia',2015],[19360,76.5,78665830,'Turkey',2015],[38225,81.4,64715810,'United Kingdom',2015],[53354,79.1,321773631,'United States',2015]]
];

option = {
    backgroundColor: new echarts.graphic.RadialGradient(0.3, 0.3, 0.8, [{
        offset: 0,
        color: '#f7f8fa'
    }, {
        offset: 1,
        color: '#cdd0d5'
    }]),
    title: {
        text: '1990 与 2015 年各国家人均寿命与 GDP'
    },
    legend: {
        right: 10,
        data: ['1990', '2015']
    },
    xAxis: {
        splitLine: {
            lineStyle: {
                type: 'dashed'
            }
        }
    },
    yAxis: {
        splitLine: {
            lineStyle: {
                type: 'dashed'
            }
        },
        scale: true
    },
    series: [{
        name: '1990',
        data: data[0],
        type: 'scatter',
        symbolSize: function (data) {
            return Math.sqrt(data[2]) / 5e2;
        },
        emphasis: {
            label: {
                show: true,
                formatter: function (param) {
                    return param.data[3];
                },
                position: 'top'
            }
        },
        itemStyle: {
            shadowBlur: 10,
            shadowColor: 'rgba(120, 36, 50, 0.5)',
            shadowOffsetY: 5,
            color: new echarts.graphic.RadialGradient(0.4, 0.3, 1, [{
                offset: 0,
                color: 'rgb(251, 118, 123)'
            }, {
                offset: 1,
                color: 'rgb(204, 46, 72)'
            }])
        }
    }, {
        name: '2015',
        data: data[1],
        type: 'scatter',
        symbolSize: function (data) {
            return Math.sqrt(data[2]) / 5e2;
        },
        emphasis: {
            label: {
                show: true,
                formatter: function (param) {
                    return param.data[3];
                },
                position: 'top'
            }
        },
        itemStyle: {
            shadowBlur: 10,
            shadowColor: 'rgba(25, 100, 150, 0.5)',
            shadowOffsetY: 5,
            color: new echarts.graphic.RadialGradient(0.4, 0.3, 1, [{
                offset: 0,
                color: 'rgb(129, 227, 238)'
            }, {
                offset: 1,
                color: 'rgb(25, 183, 207)'
            }])
        }
    }]
};

// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);
</script>

## 总榜前 100 名
### 活跃度数据

|      | repos                                     | grank  | owner                  | 
|------|-------------------------------------------|--------|------------------------| 
| 1    | qcloud-documents                          | 685.33 | tencentyun             | 
| 2    | TranslateProject                          | 112.17 | lctt                   | 
| 3    | tidb                                      | 68.82  | pingcap                | 
| 4    | apollo                                    | 58.76  | apolloauto             | 
| 5    | ant-design                                | 56.1   | ant-design             | 
| 6    | incubator-shardingsphere                  | 34.97  | apache                 | 
| 7    | gold-miner                                | 33.18  | xitu                   | 
| 8    | omi                                       | 33.07  | tencent                | 
| 9    | tikv                                      | 29.4   | tikv                   | 
| 10   | element                                   | 27.39  | ElemeFE                | 
| 11   | rax                                       | 27.32  | alibaba                | 
| 12   | skywalking                                | 25.92  | apache                 | 
| 13   | carbondata                                | 25.22  | apache                 | 
| 14   | tinkerpop                                 | 24.07  | apache                 | 
| 15   | umi                                       | 23.69  | umijs                  | 
| 16   | vant                                      | 23.21  | youzan                 | 
| 17   | RSSHub                                    | 23.18  | diygod                 | 
| 18   | taro                                      | 22.59  | nervjs                 | 
| 19   | incubator-weex                            | 22.2   | apache                 | 
| 20   | bk-cmdb                                   | 20.87  | tencent                | 
| 21   | anu                                       | 20.3   | RubyLouvre             | 
| 22   | ice                                       | 20.07  | alibaba                | 
| 23   | dubbo                                     | 19.79  | apache                 | 
| 24   | zent                                      | 19.59  | youzan                 | 
| 25   | rt-thread                                 | 19.25  | rt-thread              | 
| 26   | docs-cn                                   | 18.65  | pingcap                | 
| 27   | pouch                                     | 18.4   | alibaba                | 
| 28   | openrasp                                  | 17.33  | baidu                  | 
| 29   | iOS-Weekly                                | 16.44  | SwiftOldDriver         | 
| 30   | ModelArts-Lab                             | 15.81  | huaweicloud            | 
| 31   | incubator-doris                           | 14.87  | apache                 | 
| 32   | 996.ICU                                   | 14.79  | 996icu                 | 
| 33   | learngit                                  | 14.56  | michaelliao            | 
| 34   | docs                                      | 14.51  | pingcap                | 
| 35   | ant-design-pro                            | 14.1   | ant-design             | 
| 36   | hyperf                                    | 13.72  | hyperf                 | 
| 37   | kylin                                     | 12.42  | apache                 | 
| 38   | aliyun-openapi-java-sdk                   | 12.38  | aliyun                 | 
| 39   | vant-weapp                                | 11.69  | youzan                 | 
| 40   | Saturn                                    | 11.47  | vipshop                | 
| 41   | ant-design-mobile                         | 11.41  | ant-design             | 
| 42   | dde-control-center                        | 11.18  | linuxdeepin            | 
| 43   | pd                                        | 10.65  | pingcap                | 
| 44   | GCTT                                      | 10.09  | studygolang            | 
| 45   | articles                                  | 9.94   | ruanyf                 | 
| 46   | hiui                                      | 9.49   | xiaomi                 | 
| 47   | seata                                     | 9.19   | seata                  | 
| 48   | rocketmq                                  | 9.14   | apache                 | 
| 49   | bk-sops                                   | 8.98   | tencent                | 
| 50   | mip2                                      | 8.96   | mipengine              | 
| 51   | egg                                       | 8.88   | eggjs                  | 
| 52   | tidb-ansible                              | 8.86   | pingcap                | 
| 53   | nacos                                     | 8.85   | alibaba                | 
| 54   | incubator-echarts                         | 8.58   | apache                 | 
| 55   | mpx                                       | 8.5    | didi                   | 
| 56   | alibaba-cloud-sdk-go                      | 8.35   | aliyun                 | 
| 57   | ncnn                                      | 8.14   | tencent                | 
| 58   | incubator-dolphinscheduler                | 8.14   | apache                 | 
| 59   | dde-file-manager                          | 8.08   | linuxdeepin            | 
| 60   | aliyun-openapi-python-sdk                 | 8.01   | aliyun                 | 
| 61   | G2                                        | 7.92   | antvis                 | 
| 62   | tidb-operator                             | 7.82   | pingcap                | 
| 63   | aliyun-openapi-net-sdk                    | 7.63   | aliyun                 | 
| 64   | stellaris_cn                              | 7.51   | cloudwu                | 
| 65   | tispark                                   | 7.49   | pingcap                | 
| 66   | mip-extensions                            | 7.48   | mipengine              | 
| 67   | Dragonfly                                 | 7.39   | dragonflyoss           | 
| 68   | kubeedge                                  | 7.38   | kubeedge               | 
| 69   | wechat                                    | 7.27   | overtrue               | 
| 70   | wepy                                      | 7.04   | tencent                | 
| 71   | G2Plot                                    | 6.93   | antvis                 | 
| 72   | incubator-apisix                          | 6.85   | apache                 | 
| 73   | apollo                                    | 6.76   | ctripcorp              | 
| 74   | atlas                                     | 6.72   | alibaba                | 
| 75   | cube-ui                                   | 6.55   | didi                   | 
| 76   | mand-mobile                               | 6.35   | didi                   | 
| 77   | ant-design-pro-site                       | 6.29   | ant-design             | 
| 78   | LiteOS                                    | 6.26   | liteos                 | 
| 79   | san                                       | 6.22   | baidu                  | 
| 80   | taro-ui                                   | 6.1    | nervjs                 | 
| 81   | pandora                                   | 5.98   | midwayjs               | 
| 82   | incubator-brpc                            | 5.98   | apache                 | 
| 83   | tidb-binlog                               | 5.9    | pingcap                | 
| 84   | druid                                     | 5.7    | alibaba                | 
| 85   | AliOS-Things                              | 5.6    | alibaba                | 
| 86   | spritejs                                  | 5.57   | spritejs               | 
| 87   | canal                                     | 5.55   | alibaba                | 
| 88   | terraform-provider                        | 5.48   | alibaba                | 
| 89   | parser                                    | 5.46   | pingcap                | 
| 90   | TDengine                                  | 5.41   | taosdata               | 
| 91   | pika                                      | 5.29   | qihoo360               | 
| 92   | aliyun-openapi-php-sdk                    | 5.24   | aliyun                 | 
| 93   | G6                                        | 5.23   | antvis                 | 
| 94   | amis                                      | 5.1    | baidu                  | 
| 95   | xLua                                      | 5.1    | tencent                | 
| 96   | Kingfisher                                | 5.09   | onevcat                | 
| 97   | spring-cloud-alibaba                      | 5.08   | alibaba                | 
| 98   | funcraft                                  | 5.07   | alibaba                | 
| 99   | Sentinel                                  | 4.92   | alibaba                | 
| 100  | arthas                                    | 4.87   | alibaba                | 

### 社区化程度数据

|     | repos                                    | grank | owner                  | 
|-----|------------------------------------------|-------|------------------------| 
| 1   | sofa-pbrpc                               | 1     | baidu                  | 
| 2   | COLA                                     | 1     | alibaba                | 
| 3   | ali-rds                                  | 1     | ali-sdk                | 
| 4   | QMUI_Web_Desktop                         | 1     | tencent                | 
| 5   | ai-matrix                                | 1     | alibaba                | 
| 6   | antd-init                                | 1     | ant-design             | 
| 7   | bugCatcher                               | 1     | youzan                 | 
| 8   | chaosblade                               | 1     | chaosblade-io          | 
| 9   | umi-plugin-qiankun                       | 1     | umijs                  | 
| 10  | wafer2-quickstart                        | 1     | tencentyun             | 
| 11  | laravel-uploader                         | 1     | overtrue               | 
| 12  | aliyun-openapi-java-sdk                  | 1     | aliyun                 | 
| 13  | tac                                      | 1     | alibaba                | 
| 14  | fish-redux                               | 1     | alibaba                | 
| 15  | mooa                                     | 1     | phodal                 | 
| 16  | linden                                   | 1     | xiaomi                 | 
| 17  | InjectFix                                | 1     | tencent                | 
| 18  | alipay-sdk-python-all                    | 1     | alipay                 | 
| 19  | iot                                      | 1     | phodal                 | 
| 20  | intl-example                             | 1     | ant-design             | 
| 21  | aliyun-oss-react-native                  | 1     | aliyun                 | 
| 22  | QMUI_Android                             | 1     | tencent                | 
| 23  | Resume                                   | 1     | diygod                 | 
| 24  | LuaPanda                                 | 1     | tencent                | 
| 25  | launch-editor                            | 1     | yyx990803              | 
| 26  | dal                                      | 1     | ctripcorp              | 
| 27  | GoodNight                                | 1     | diygod                 | 
| 28  | laravel-pinyin                           | 1     | overtrue               | 
| 29  | logkafka                                 | 1     | qihoo360               | 
| 30  | fde                                      | 1     | phodal                 | 
| 31  | Logan                                    | 1     | meituan-dianping       | 
| 32  | father                                   | 1     | umijs                  | 
| 33  | omi-cli                                  | 1     | alloyteam              | 
| 34  | skynet                                   | 1     | cloudwu                | 
| 35  | go-spring-doc                            | 1     | didi                   | 
| 36  | free-programming-books-zh_CN             | 1     | justjavac              | 
| 37  | ins                                      | 1     | baidu                  | 
| 38  | g6-editor                                | 1     | antvis                 | 
| 39  | edp                                      | 1     | ecomfe                 | 
| 40  | rtthread-manual-doc                      | 1     | rt-thread              | 
| 41  | Programming-Alpha-To-Omega               | 1     | justjavac              | 
| 42  | Virtualview-Android                      | 1     | alibaba                | 
| 43  | VasSonic                                 | 1     | tencent                | 
| 44  | HandyJSON                                | 1     | alibaba                | 
| 45  | alita                                    | 1     | areslabs               | 
| 46  | weex-vue-starter-kit                     | 1     | ElemeFE                | 
| 47  | alibaba.github.com                       | 1     | alibaba                | 
| 48  | egg                                      | 1     | eggjs                  | 
| 49  | weui-wxss                                | 1     | tencent                | 
| 50  | Weibo2RSS                                | 1     | diygod                 | 
| 51  | WeDemo                                   | 1     | tencent                | 
| 52  | metrics                                  | 1     | alibaba                | 
| 53  | cachecloud                               | 1     | sohutv                 | 
| 54  | justjavac.github.com                     | 1     | justjavac              | 
| 55  | pbc                                      | 1     | cloudwu                | 
| 56  | document-style-guide                     | 1     | ruanyf                 | 
| 57  | AlloyFinger                              | 1     | alloyteam              | 
| 58  | freeline                                 | 1     | alibaba                | 
| 59  | fonteditor                               | 1     | ecomfe                 | 
| 60  | wisteria                                 | 1     | overtrue               | 
| 61  | OwO                                      | 1     | diygod                 | 
| 62  | awesome-echarts                          | 1     | ecomfe                 | 
| 63  | sofa-rpc-node                            | 1     | sofastack              | 
| 64  | ChromeSnifferPlus                        | 1     | justjavac              | 
| 65  | RedisShake                               | 1     | alibaba                | 
| 66  | ant-design-pro-layout                    | 1     | ant-design             | 
| 67  | wafer-node-server-demo                   | 1     | tencentyun             | 
| 68  | Shield                                   | 1     | meituan-dianping       | 
| 69  | wechat                                   | 1     | overtrue               | 
| 70  | chartx                                   | 1     | thx                    | 
| 71  | oss-browser                              | 1     | aliyun                 | 
| 72  | config-toolkit                           | 1     | dangdangdotcom         | 
| 73  | fks                                      | 1     | JacksonTian            | 
| 74  | aliyun-log-jaeger                        | 1     | aliyun                 | 
| 75  | vno                                      | 1     | onevcat                | 
| 76  | wafer2-client-sdk                        | 1     | tencentyun             | 
| 77  | FengNiao                                 | 1     | onevcat                | 
| 78  | smart-gesture                            | 1     | ElemeFE                | 
| 79  | ARouter                                  | 1     | alibaba                | 
| 80  | egg-graphql                              | 1     | eggjs                  | 
| 81  | anyproxy                                 | 1     | alibaba                | 
| 82  | tencent-ml-images                        | 1     | tencent                | 
| 83  | magix-inspector                          | 1     | thx                    | 
| 84  | debugtron                                | 1     | bytedance              | 
| 85  | Pretrained-Language-Model                | 1     | huawei-noah            | 
| 86  | laravel-emoji                            | 1     | overtrue               | 
| 87  | SoloPi                                   | 1     | alipay                 | 
| 88  | pipcook                                  | 1     | alibaba                | 
| 89  | clean-frontend                           | 1     | phodal                 | 
| 90  | macaca                                   | 1     | alibaba                | 
| 91  | road                                     | 1     | ruanyf                 | 
| 92  | learngit                                 | 1     | michaelliao            | 
| 93  | rexxar-web                               | 1     | douban                 | 
| 94  | gbdt-rs                                  | 1     | mesalock-linux         | 
| 95  | antvis.github.io                         | 1     | antvis                 | 
| 96  | pod                                      | 1     | yyx990803              | 
| 97  | bagpipe                                  | 1     | JacksonTian            | 
| 98  | DBProxy                                  | 1     | meituan-dianping       | 
| 99  | funcraft                                 | 1     | alibaba                | 
| 100 | GCTT                                     | 1     | studygolang            | 