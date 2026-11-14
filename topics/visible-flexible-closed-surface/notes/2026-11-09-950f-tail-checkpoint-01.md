# 冻结数值批次 950f-tail-01

本批次是冻结 K6/width .45 weighted metric 的有限尾数值计算；不是完整闭族。
M4/depth10/steps64/quad128：a=.0003 收敛，shoot1.7671544e-9，fullD7.311443e-5，
actualMetric1.181838e-7，minA .8203489，formalCurvature6.128973。
从此直接倍增至 a=.0006 时初值D/S/A分支拒绝；该失败仅是本次Newton初值诊断。
全部成功和失败请求均保存原始压缩响应，原始full trace已完整结束且冻结。

线性接口由momentum坐标计算m3…m288。cusp-aware s512→1024：
m3 DN=10.576513803204914，两级差6.6983e-11；全96最大差4.1088e-5，
最高频尚须按实际输入的误差传播审核。旧uniform结果也保留，未混作同算法。

运行命令（从任意目录；SOURCE为完整本仓库 checkout）为：

python scripts/950f-tail-run.py --config notes/2026-11-09-950f-tail-k6-m4-config.json --source-root SOURCE --out NEW_RESULT.json

需将config traceFile改为新的工作输出路径（只影响日志，不改变metric）。
完整输入、结果及已读源码sha256/尺寸见同名manifest.json。
manifest内external_dependency文件为仓库现有只读来源，不需重复上传。

仍在跑的M4细步和M8角加密不计入本冻结批次。下一批将独立记录。
