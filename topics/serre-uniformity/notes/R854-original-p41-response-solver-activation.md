# R854 原41四响应首跑请求

状态：执行方法已证明；本文件登记首次实际求值请求，**尚无41数值结果**。会话 serre-public-astra-20261115，2026-11-16。

## 原问题与来源

直接求 [R854 全行方法](R854-original-41-cleared-row-saturation-and-four-responses.md) 的同一 2420 未知原 U.1，free1186=1、其余27个free为0，保已带负号的 Z 与原四泛函。几何整化严格用[补节](R854-original-41-geometric-row-scaling.md)，实际左逆界属于 M0=S M；完整残差逐行扣回及加权恢复，不冒称原未加权精度。

直接父来源为已成 R849 run43790410670/source391191590dcb8bcc6f8f2d777610726fa79dc2a3 与 R847 run43789012126/sourcef699023d15daacb7d7e176f52da41899d69ae26c。全部 artifact/run/source/manifest 和子来源 SHA 在同目录公开 request 中固定。首跑先核原395061658字节 GLOBAL 载体及2709成员，再只保实际所需1375个R781/R787叶、270个POINTS叶及20个父元数据，共1665件。仅本地核了已取得的1645原叶和20元数据的 IO；不声称本地下载过大载体。

## 已提交的确定性执行程序

| 部件 | SHA256 |
|---|---|
| 原41 core | `1feb579a88879739a250f889ab1818019acb8f1156a0e3f34d57b8524024125f` |
| DVR 线性代数 | `fa545b181fa5b77758622d1862adfd4445cd05d44fdc65dda92f738ebe522c0d` |
| 公开 wrapper | `f6b97a7d0640a03fa099d3b0b04541318e53ddbcf611a876f877b3dc42c7f0ae` |
| 原 R787 多项式域核心 | `93d3d72b01b0ed5d48486a632b74c3470b15affdcb1bd03e21f1b5283fc82d04` |
| 公开 request | `f6cfe6fbd6a1405a3668a56ea18cde6ba0767e1b344ab5e055918e5c8d5f7878` |
| workflow | `9105ed2e4bc41df451c37272d2fb081c3b94ec4922dbd1f169fd59dc1fd74bd6` |

首请求预算300分钟、operator_B_precision=56、requested_response_B_precision=7、列块8、行块32、resume=null。56与7是精度控制，不是已达到的结论。所有新增数学只由公开 workflow `serre-R854-original-p41-response-solver.yml` 执行；数学库固定 python-flint==0.9.0。

同一 source tag 下保存已成算子块、行饱和变换、实际单位子式及其逆、逐位 Dixon 事务、完整残差向量和四响应。真正完成的旧位、行变换不重算；提高精度时只取得新的精度层。弃用工作矩阵须有完整 SHA 的 retirement receipt；不可删旧数学依据。wrapper 在外层时限前保留上传机会，缺 receipt 或不足精度如实标未成。

## 成功出口与后继接口

成功必须有原2560行/每行14坐标完整残差、实际左逆范数界，以及已扣分母和泛函尺度后达到请求的统一绝对 B 精度。顺序为 A0,A1,B0,B1；十四坐标为 B^0,…,B^6,sB^0,…,sB^6，实际值是 numerator/(B^delta 41^h)。`absolute_B_precision` 是最终球精度，不是 numerator 存储精度；原 integer_scale 不再施一次。不能预设 B0 为41单位。

原 A.1、准确特征零展开、一个 Z、Y 或高度均不由本请求预先接受。后继 R858 只消费实际认证的四响应和原 R852 五 C/D 来源。程序、参数、run 与输出 SHA 入库；机器数据仅保一日必要 artifact，不进 Git/Release。
