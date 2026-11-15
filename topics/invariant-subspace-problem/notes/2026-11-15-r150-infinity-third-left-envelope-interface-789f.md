# R150：完整第二连接零之后的原无穷远第三左延拓入口

日期：2026-11-15 UTC。Astra-ISP-789f；AI-assisted，GPT-6 Astra Pro。

## 唯一新增数学与原来源范围

保持同一自然参数 $u=1/s$、原物理反序及共动矩变换。已付第一连接秩四、第二连接零，因此完整第三页目标维数二十三。十个纯切向泛函的 $d$ 次数至多一；原十七式沿切向平面的所有纯项均被 $d^2$ 整除，故这十个泛函沿全部参数严格为零。其余十个纯泛函及三个横向泛函使用已付完整二阶规范，不能随意丢弃校正项。

本次只新增原 $u^3$ 系数及十三个第三残差。纯三阶项为
$d^2(80,128,96,48)$，分别放原 $N_7,N_8,N_9,N_{10}$。
保
$$
R_3=A_3^{\mathsf T}\lambda_0+A_2^{\mathsf T}\lambda_1+
A_1^{\mathsf T}\lambda_2;
$$
特别保留 $A_2$ 的纯项与 $\lambda_2$ 的完整二横向部分。
残差仍只支持 $170+918=1088$ 行；其余 $5100$ 个原来源严格按横向次数为零。

固定旧 $[J_0,A_1^{\mathsf T}Q]$ 后，一次新的 $1088\times605$ 有理 RREF 求三阶左校正。全部旧原系数、二阶增广矩阵、纯/横向规范校正哈希和全行乘回均保留。若十三列新增秩为 $k$，仅推出
$$
\operatorname{rank}\beta_3\le\min(10,k),\qquad
\delta_{4354,\infty}\ge\max(34,44-k),\quad
\delta_{4353,\infty}\ge\max(31,40-k).
$$
正残差不自动给完整连接下界，也不排更高横向校正。实际结果前不更新任何 Smith 数字。

## 源码与实际运行参数

脚本 [2026-11-15-r150-infinity-third-left-envelope-789f.py](2026-11-15-r150-infinity-third-left-envelope-789f.py)
SHA256 为
eaad9fbcecd3035965de02c9e20e2c4a2372641f3bf6a97a0b99422887bf7d93。
复用第一生成器 SHA2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186，
第二生成器 SHA6cb201867c430b4375dbe93cb411ad1e74bea39571261d1ecfec233e4b397517。

在现有临时 session 43679903558 排 step infinity-third-left-envelope：
~~~text
--generator {scripts}/2026-11-15-r150-original-transverse-first-connection-789f.py
--normal-generator {scripts}/2026-11-15-r150-infinity-second-normal-envelope-789f.py
--first-connection-receipt {work}/original-transverse-first-connection-receipt.json
--second-pure-receipt {work}/infinity-second-pure-envelope-receipt.json
--second-normal-receipt {work}/infinity-second-normal-envelope-receipt.json
--out {work}/infinity-third-left-envelope-receipt.json
--remaining-seconds 30
~~~

数学共享时钟三十秒、地址空间512MiB、外层八十秒含收尾。这是本次具体预算；未完成须保实际阶段继续，不是课题收尾理由。只保存源码、参数、run ID、哈希和小回执；所有可重算矩阵在作业内临时使用。
