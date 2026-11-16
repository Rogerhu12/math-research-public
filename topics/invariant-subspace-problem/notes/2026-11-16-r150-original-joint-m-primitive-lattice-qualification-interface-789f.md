# 原九目标共同模 M 的整自由格资格检查：完整 225 列与真 16 维系数扭子

作者：ChatGPT（AI），literature_audit  
日期：2026-11-16  
状态：源码与参数冻结；本检查尚未实际运行，不预填任何新秩。

## 1. 原问题与已完成输入

仍用完整原矩阵 $A\colon D[s]^{6188}\to D[s]^{4367}$，
$D=\mathbb Z_{(31)}$、$p=31$、$x=s-2$。
令 $N$ 为原泛像饱和模，$C=N/\operatorname{im}A$，
$T=C[p^\infty]$，$M=\sum_{j=2}^{10}D[s][t_j]$。

两个直接父结论是：

- [完整九目标整湮灭理想](../results/R150-appendix-original-nine-targets-complete-integral-annihilator-and-parameter-denominator-law.md)：
  $\operatorname{Ann}M=h_*(p^5,p^2x,x^2)$。
- [共同 B 的完整类型与八生成元](../results/R150-appendix-original-joint-nine-target-coefficient-module-length24-and-eight-generators.md)：
  $B=h_*M$ 的 $D$ 型是 $(1^6,2,3,4,4,5)$，长度 $24$。
  这没有把 $M\cap T$ 与 $B$ 等同。

完整 $T$ 的真除源基有 16 列，指数为
$(1,1,2,2,2,2,2,3,3,4,4,4,4,5,5,6)$。
其模 $p$ 原完整 315 坐标基、参数作用分别固定为 SHA-256：

- U16：679132fd4727fd305b77c82beb5d3f2e002df1860045200c3392158ab8eb48b9。
- J16：59d09cbeec71ebf7cda6f12ddd21c1b7ffe1c83a3f9de81b776df0a97df687d8。

这些是完整系数扭子，不是点核或低阶来源切片。
本次决定：九目标在 $C/T$ 中的整自由格，能否由实际原目标列作饱和基。
只有资格成立后，后继才能据此去除真实自由部分并恢复系数扭子余量。

## 2. 完整 225 列

已付 $x^2h_*M=0$，而 $x^2h_*$ 次数 $25$、首系数 $3125$ 为 $D$ 单位。
因此
$$
M=\sum_{j=2}^{10}\sum_{k=0}^{24}D\,s^k[t_j].
$$
这是完整 $D$ 生成族，不是有限次数猜测。

消费者从固定完整状态读出原九列 $\Xi$ 和原参数作用 $J$，构造
$$
V=[\Xi,J\Xi,\ldots,J^{24}\Xi]\in\mathbb F_{31}^{315\times225}.
$$
先核 $K\Xi=T_{\rm original}$、$AK=KJ$、
全部 $505$ 自由观测对 $K$ 为零，再核全部 225 列的参数闭包，
以及 $(J-2)^2h_*(J)\Xi=0$。
字典顺序是先 $k$，后原标签 $j=2,\ldots,10$。

所有 315 坐标保留，没有先投到 root2，也没有用旧 U7 代完整 T。
域状态中额外的一维缺陷，不被宣称为原 $C/T$ 的自由方向。

## 3. 自由格资格引理

已付 $C$ 是有限 $D$ 模，$F=C/T$ 为有限自由 $D$ 模。
完整原来源链给出
$$
C/pC\hookrightarrow\operatorname{Tor}(\operatorname{coker}\bar A).
$$
由于 $F$ 自由，
$$
0\longrightarrow T/pT\longrightarrow C/pC\longrightarrow F/pF\longrightarrow0.
$$
所以用实际 U16 商掉完整域像合法：
$F/pF$ 注入完整 315 维空间再商 U16 的空间。
不要求后者的每个方向都来自 $F/pF$。

已付 $\dim_{\mathbb Q}M_{\mathbb Q}=25$。
若实际 $V\bmod U_{16}$ 秩为 $25$，选出 25 个独立原列，
其在 $F$ 中的像记为 $f_1,\ldots,f_{25}$。
它们模 $p$ 独立，所以
$F_0=\sum Df_i$ 是 $F$ 的直和项，特别
$$
F\cap\operatorname{span}_{\mathbb Q}(f_1,\ldots,f_{25})=F_0.
$$
全部 $M$ 的自由像都在这个有理空间，故全在 $F_0$。
以原 25 列提升，得到
$$
M\simeq_D D^{25}\oplus(M\cap T).
$$
这里只断言 $D$ 模分裂，没有断言参数 $s$ 保持这个分裂。

若实际秩不足 $25$，检查正常报告该数；不证明有理秩变小或成员失败，
也不把不足的列当整基。

资格通过时，自由像实际特征多项式还须逐系数等于
$$
\overline{s^2\operatorname{mon}(h_*)}.
$$
这是一致性门，不代替秩计算。

## 4. 两个系数扭子主分量

完整 $T/pT$ 的支持是 $s=1,2$，
对应 $D$ 型分别为 $(1,2)$ 和
$(1,2,2,2,2,3,3,4,4,4,4,5,5,6)$。

程序从整个 $J$ 的特征多项式构造真正 CRT 投影，
再在 $\langle U_{16},V\rangle$ 的实际不变子空间求值。
每个投影均核幂等、交换、正交、总和为一及原 315 坐标运输。
不由一个点的秩冒充完整局部模。

在 $\widehat D=\mathbb Z_{31}$ 中，原 $h_*$ 在两处都有唯一简单 Hensel 因子
$s-\alpha_a$，$\alpha_a\equiv a\pmod p$。
原整数小检验为
$$
h_*(1)=-387688964096,\quad h_*(1)/31\equiv24,\quad h_*'(1)\equiv8;
$$
$$
h_*(2)=17886115659776,\quad h_*(2)/31\equiv20,\quad h_*'(2)\equiv19
\pmod{31}.
$$
故 $h_*$ 在两个系数扭子主分量上均不能直接作为单位约去。

每处自由目标的有理维数恰一。
若实际原九列在完整自由商中秩一，选非零原 $t_j$ 作 $f$。
同上一节，$\widehat Df$ 在该一维有理线内饱和，
所有目标自由部分都属该真整格，得到
$$
\widehat M_a\simeq_{\widehat D}\widehat Df\oplus
(\widehat M_a\cap\widehat T_a).
$$

在 $a=1$，$x=s-2$ 为单位，已付湮灭式给
$(s-\alpha_1)\widehat M_1=0$，九个原目标是完整 $\widehat D$ 生成族。
在 $a=2$，令 $\beta=\alpha_2-2\in31\mathbb Z_{31}$，则
$$
x^2(x-\beta)\widehat M_2=0.
$$
所以 $t_j,xt_j,x^2t_j$ 共 27 列是完整 $\widehat D$ 生成族。
这是生成族大小，不是独立性或最少生成元声明。

后继 carry 若用 primitive 自由列，还须保留
$$
p^6\widehat C\cap\widehat Df=p^6\widehat Df
$$
和 $p^6T=0$。
六位自由系数的尾项因此可吸收到真实自由列中，不能当作零。

## 5. 可以直接免去高精度 carry 的实际门

令 $V_a$ 为某主分量的实际域目标像，$\bar T_a$ 为完整系数扭子约化像。
primitive 自由线资格成立时，
$$
V_a\cap\bar T_a
$$
正是 $\widehat M_a\cap\widehat T_a$ 在
$\widehat T_a/p\widehat T_a$ 中的像。

逆向包含的理由是：
若一个目标组合自由部分模 $p$ 为零，真自由部分为 $pcf$；
减去 $pcf$ 后仍属 $\widehat M_a$，模 $p$ 影像不变，而且成为真正系数扭子。

因此只有实际
$$
\dim V_a-\dim(\text{自由像})=\dim\bar T_a
$$
成立，Nakayama 才给
$\widehat M_a\cap\widehat T_a=\widehat T_a$。
程序有单独布尔门。若不足，只报告真实像，
不把它当成完整扭子模的维数或不变量因子。

全局若自由资格为 25，实际原域目标维数为 $25+16$，
同理得到 $M\cap T=T$。
本接口没有预报这些等号成立。

## 5a. 完整域目标像的最少生成数

程序还输出完整域目标像的参数作用 $J_M$ 的特征多项式、最小多项式，
以及 $J_{16}$ 的对应两式。对每个不可约因子 $f$，
在真实完整主分量 $V_f$ 上计算
$$
g_f=\frac{\dim_{\mathbb F_{31}}V_f-
\operatorname{rank}f(J_M|_{V_f})}{\deg f}.
$$
这等于该主分量作为 $\mathbb F_{31}[s]$ 模的最少生成数。
程序核整除性、每项不超过九，并核所有主分量的特征式与最小式分别复乘成完整原式。
令 $g=\max g_f$。

原 $M$ 到该完整域目标像的满射给出 $d_{D[s]}(M)\ge g$。
结合已付共同 $B$ 的八生成元下界和原九目标上界，
本次严格输出
$$
\max(8,g)\le d_{D[s]}(M)\le9.
$$
只有实际 $g=9$ 才标记原 $M$ 恰需九生成元；
若 $g<9$，仍保留原区间，不从域像的较少生成元反推整模可以减少。
此推论不要求第3节的自由格资格先成立，也不借用未求的高精度扭子坐标。

## 6. 父输入边界

只接受已完成父 binding：
0a0b38c3107add8f719b0fac0d99ec75f44c48d842b830dadb1ed1e7b1f84ce1。

父源码为 2026-11-16-r150-joint-b-true16-source-rebuild-p9-789f.py：
38570 B，SHA-256
e4b2b935882e899a55d7db10d590e5ce8d35f5fedcab6063a14008a5efe4b69e。

新 job 须先真实执行同一个 8→7→3→1、35→30→25→20→15 的 30 阶段父重建。
父 run 43841516263 已结束，本接口不声称旧临时目录仍在。
不重 full210，不重 NF/GB 消元。

消费者核对实际完成 receipt、pack、30 stage 与 binding；
四个完整 315 类文件的 bytes/SHA 与 104/315/505 门；
完整 recipe payload、原 whole state；
重组 U16/J16；
全 225 原目标、各主分量和原 820/505 运输。

程序只读父数据，不改父文件。
新完整资格数据仅存自己的临时 out，供同 job 后继消费。
仓库仅存源码、参数、run、SHA；矩阵不进 Git、Release 或新工件。

## 7. 冻结文件

源码：2026-11-16-r150-original-joint-m-primitive-lattice-qualification-789f.py

- Blob：35cfecb0fc77010d6296aea67f9f073d191dd437。
- 22918 B。
- SHA-256：855614a779dca566478752179e68710934cc2982eef3a4b60452119a0ff3cf01。

Request：2026-11-16-r150-joint-m-qualification-session-789f-request.json

- Blob：40d36dafbd25fcc2b3b92880a751586058295cd0。
- 9158 B。
- SHA-256：38763edf7853212b52efb8cfb01fcdd50479a67d555b4ebbb85a1e10961588e2。

Wrapper 只将已成功 joint-B worker 的 request、临时前缀与身份目录改名：

- Blob：e01db952b8a3bfbe0e89822ddca2e8c42b01c7ae。
- 15432 B。
- SHA-256：5589df0e449d3d87d2156331eea474760d7745b75d537bf2fbdc9d0834c61281。

Workflow：.github/workflows/invariant-subspace-r150-joint-m-qualification-session.yml

- Blob：1773187a4df6b4689ed945ec9c6167ba17084a2a。
- 1348 B。
- SHA-256：5f6c8090391887a7de7a566f4f9566169429a6b47b3a132051a84c341db7026e。

## 8. 同 job 执行

五任务为原 14 文件恢复、六 small 恢复、四族/原整数/jet-map 恢复、
已付 p9 选列重建、新资格检查。前四任务数学源码与输入不改。

~~~sh
python 2026-11-16-r150-original-joint-m-primitive-lattice-qualification-789f.py \
  --notes-root "$scripts" \
  --parent-out "$work/joint-b-selected-true16" \
  --state "$work/global197-original-inputs/state.bin" \
  --recipe "$work/joint-b-selected-true16/prepared210/complete210-fourth-source-recipes.json.gz" \
  --out "$work/original-joint-m-qualification" \
  --seconds 120 --memory-mib 2048
~~~

receipt 位于 out/original-joint-m-primitive-lattice-qualification.json。

总 job 180 分钟，worker 有限循环 170 分钟。
检查本身 120 秒/2 GiB，外层 150 秒。
父重建沿已付 1800 秒/4 GiB，仅 exit75 同绑定续接。

本次 closeSessionWhenStepsComplete=true、idle60：五步结束即完成 job，
随后从完整 job 日志读取实际数学结果，不为尚不能读取的运行日志空等。
父临时数组在 job 结束后不再视为可用。
若资格后确需 p12 高精度后继，则另 job 真实重建最小同源父；不重 full210。
异常同时记录在顶层与 parameters.error，避免小身份消毒丢失错误原因。

只有真实恢复、重建与资格门通过后，才记录新数学身份。
当前仍是未运行的可执行方案。
