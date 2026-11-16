# 负四 kk 的两个剩余完整自然泛函：最小新观察

日期：2026-11-16。本文件是尚未执行的源码与请求设计。研究执行由根代理唯一调度公开 Actions；没有本地执行、旧人工重跑或新 profile 取值。

## 1. 已闭结构与本次两个目标

[R427](../results/R427-even-quartic-curvature-support-of-the-complete-kk-minus4-natural-function.md) 从原完整恢复证明

$$
\mathcal N\!\left([h^{-4}]\widehat Q_{kk}(h,k,0)\right)
=\mathcal N(V_0)+k^2\mathcal N(V_2)+k^4\mathcal N(V_4).
\tag{1}
$$

这里取 $\omega^0(\log h)^0$，原 family 是 $Q2_0$，真实成本权为 $-4$。这是完整自然函数身份，不是原 $U$ 元素只含这三个系数的断言。

本次仅观察两个独立尚未知的原系数

$$
B=V_2=[h^{-4}k^2\omega^0(\log h)^0]\widehat Q_{kk},
\qquad
C=V_4=[h^{-4}k^4\omega^0(\log h)^0]\widehat Q_{kk}.
\tag{2}
$$

$k=0$ 锚由独立原式工作处理，不在新运行中重算。也不先假设 $S=1+k^2$ 整除：由 (1)，该整除恰要求

$$
\mathcal N(V_2-V_0-V_4)=0,
\tag{3}
$$

目前它不能由低一权、单锚或原 pure 坐标推出。

本次沿已付 HH4 观察的 reader、typed self 代入和 frozen R406 通量 mapper，只改变两个目标及原 kk 水平方向。没有新增旧空间秩、旧 pure 映射、原 forcing 编译或完整 mixed 家族重建。

## 2. 原 kk 水平导数必须先于 $\omega=0$

原完整正规槽为

$$
\widehat Q_{kk}
=[k_s^2]\{v^{[2]}-B_{m_0}(N^{[2]})
-B_{m_2}(N^{[0]})-\Gamma(m_2)\}
-Y[k_{ss}]v^{[2]},
\qquad
Y=\partial_k+\frac1{2h}\partial_\omega.
\tag{4}
$$

源几何键按 $(h,k,\omega,\log h)$ 和
$(h_s,k_s,h_{ss},k_{ss},h_{sss},k_{sss})$ 分开。

对原加速度系数 $h^a k^b\omega^c(\log h)^d\,v$，程序准确保留

$$
-Y\!\left(h^ak^b\omega^c(\log h)^dv\right)
=
-b\,h^ak^{b-1}\omega^c(\log h)^dv
-\frac c2\,h^{a-1}k^b\omega^{c-1}(\log h)^dv.
\tag{5}
$$

$Yh=Y\log h=0$。两个分支作用后才匹配 (2) 的目标状态；特别是原 $\omega^1$ 行会通过第二分支进入 $\omega^0$。不能先将原根限制到 $\omega=0$，也不能把 $Y$ 改成 $\partial_k$。

所有选中的原 root 名、原 hash、几何键、导数角色及完整有理系数逐项进入公开 report。输入原 producer 已先作真实 $s$ 导数、再取局部 history 初值；新程序不改变该语义。

## 3. 两类正规势都保留完整 raw self

在原 $q=\bar q=u$ 对角，R78 的字面公式是

$$
(B_E N)_{-2}(u,u)
=-\frac12 N(\Phi_E(u,u);u,u).
\tag{6}
$$

因此 (4) 的两个负势项，在 $M_{-2}$ self 中均贡献

$$
+\frac12\,m_E\,N(\Phi_E(u,u);u,u).
\tag{7}
$$

程序扫描整个原 potential metadata，以 $N^{[0]}m_2$ 或 $N^{[2]}m_0$ 的总速度槽 $(0,2)$ 和目标标量幂筛选。每个必要 typed 原根按真实 profile 权提取，再完整代入外槽 $a=\Phi_E(u,u)$、内槽 $b=c=u$。相同 typed hash 和 $E$ 在两个目标中只装配一次并共用缓存。

$\Phi_E(u,u)$ 的真实左二次尾以及各层同一右锚积分全保留。此步骤不能只用 diagonal $N(u;u,u)$ 反猜外槽，也不能把单包输出假设为紧。

R367 的 $C_A/N_2$ 成对消项是在完整自然函数与真实尾一起收集后成立；它不意味着两项 raw self 或 pure 各自为零。本次**不在装配 raw self 前删去该配对**，从而后续使用原 R210 完整 pure 坐标仍与原输入一致。

全 $k$ 的 $-B_{m_2}N_0$ 包括 R423 的四类原势项，不能仅保留 $k=0$ 的 $B_S\tau_0/16$。新程序从完整原 metadata 选取，未用锚值简化它们。

## 4. $\Gamma$ 和固定参考项的 kk 专属支撑

本次目标是 $h^{-4}$，不能直接复用 HH4 中“整个 $m_2$ 最低 $h^{-4}$，所以不含 $h^{-6}$”的证明。

程序先从原八坐标矩阵中严格筛出 $k_s^2$ 速度槽。该槽是

$$
m_{2,kk}=\frac{kP}{16h^3}-\frac{M_z}{16h^2},
\qquad
P=J(u''^2),\quad M_z=J((x+\omega)u''^2).
\tag{8}
$$

其标量 $h$ 幂均不低于 $-3$。$\Gamma(m_{2,kk})$ 为同一组 scalar 的固定线性像，因而没有 $h^{-4}$ 项。原 $N_0$ 在固定参考点的减项本身不含当前几何状态；乘 $m_{2,kk}$ 后同样没有目标 $h^{-4}$。

源码输出整个 $m_2$ 状态列表和单独的 kk 列表，并在实际输入中核实 kk 列最低 $h$ 幂至少为 $-3$。若不满足则停止。此处没有声称 $N_0$ 左紧，也没有用其它速度槽的幂界代替本槽。

## 5. 精确复用两条 paid pure 行

唯一既付 pure 入口是 R210：

- run：43688302217；job：132733352458；
- source：1b032593b46210e7a0599a224d5c2110fe1d1606；
- 完整原 stdout：127473 bytes，SHA256 0cdf6ffa15b97cf926dad70b869945a782ee153dac317ec080d1b9d15c9030d6；
- 原 main JSON：53292 bytes，SHA256 aeea36d3c46f934ec784460367813ef7902f85f1c3492e575152fd6906e7a76a；
- 原 metadata receipt：47378 bytes，SHA256 f739e4a0ccdcf5ea102a9deb5794486b8f9f022975764e23fd14b16ec6d722c4。

原 family 下标 $1$ 是 $Q2_0$。

| 目标 | 状态 | normalized 列 | global 列 | 原 scale |
|---|---|---:|---:|---:|
| $B=V_2$ | $(-4,2,0,0)$ | 35 | 75 | $-9/8192$ |
| $C=V_4$ | $(-4,4,0,0)$ | 36 | 76 | $-5/8192$ |

$B$ 的归一 pure SHA256 为 5207d498d5664d2c9a818f2d2e00fcae4647ae767aeb240d810229e7cb23d078；其 MATHEMATICAL_COLUMN 原 tag、空格、JSON、LF framing 为 369 bytes，SHA256 29b61fd75020acf412ee0126cd8f44e04576009b703f45bac7dcaa60eb4f57f8。

$C$ 的对应 pure SHA256 为 729222403e2b54b7b2c9637cf1069d6892294cb834a4f56d5515c053789a855d；原 framing 为 380 bytes，SHA256 2ae962de1560d503c7e4ea92f47c2faef682e9aa4ea0c17729bd882ebf65af35。

两条原归一坐标为

$$
\begin{aligned}
B:\;&(0,160/9),(1,256/9),(2,-1088/9),(8,496/3),\\
   &(9,16/9),(12,-728/9),(14,-80/9),(16,-104/9);\\
C:\;&(0,192/5),(1,416/5),(2,-2016/5),(3,-52/5),\\
   &(8,2392/5),(9,168/5),(12,-248),(14,44/5),(16,-248/5).
\end{aligned}
\tag{9}
$$

每行先乘对应原 scale。retained-order 将 global $14,16$ 映到旧 R139 的 $15,17$；合并后仍只需九个旧响应下标

$$
0,1,2,3,8,9,12,15,17.
\tag{10}
$$

程序读取精确旧行、MATHEMATICAL_RESULT、EXECUTION_STATUS，并核 run/job/source/完整 log 哈希和原 family、retained-order。只消费已经付费的结果，不重求坐标或其旧秩。

## 6. 原因子与九响应输入

完整原因子：

- run 43651096112，source 2259b57065cfad67682f4c4319885fd5334c4f76；
- notes/actions-43651096112-1-local_fourth_derivative_factors/；
- main：5477 bytes，SHA256 42289590f4e8319d2bd4b138497702b701a11c4bcf39ba4c7ed0c2616f3aa927；
- receipt：33580 bytes，SHA256 6857ea6edb3b8132147e3c0c698f79aa6f29e3b59272850267875f45a07fe95e；
- gzip：2132064 bytes，SHA256 9daddeaf6ad8e7aa647df4f8084ec803625c589bfc51f595ff0d9c680ce0dd4a；
- 解压 JSON：11864540 bytes，SHA256 58e450c47123fc682f665fffb2bb66829d9d37f502b7163e2875089b72f93fd3。

原输入含 172 个 potential、3802 个 local 记录，共 3974 个带原 hash 的根。这里只扫描 metadata，按 (2)、(5)、(7) 选择必要根与依赖；不解码其余根，不调用任何原 forcing producer。

九响应来自 R139 的同一冻结导出：

- run 43654534244，source 1177f251dc3d9455adf88b585e4c0e4bd6f7e69b；
- notes/actions-43654534244-1-g_translation_successor/；
- gzip：76352 bytes，SHA256 b266eebf27d001ef90fcc94f8b49b9f9984ed5d3f7a047d9b5cef5ddffd2423b；
- 解压 JSON：427950 bytes，SHA256 6e19e56d879eed7f7d741957526679521f65f06b92c42b4cb29f39fb2c2276e4。

输入读取和 selected-DAG 恢复沿已付 HH4/W4 reader。新程序只调用原 literature_complete_pure_minus6_projection.py 的只读 subset_decode，不调用它的研究入口。每个选中根的原 digest、类型、真实权和原 self 对角 hash 均输出。

## 7. 从完整 self 到新 $\Omega$

从每个完整原系数减去 (9) 的已付响应，得到 $\pi\widehat V=0$，自然泛函不因响应改变。原规范为

$$
\widehat V(u^2,0)=-4M_{-2}^{\widehat V}(u,u).
$$

frozen R406 mapper 精确计算

$$
\Omega_u(\widehat V)
=-4\int u'''M_{-2}^{\widehat V}(u,u)
=4\left[I_r^x\!\left(u'''M_{-2}^{\widehat V}(u,u)\right)\right]_{\mathrm{left}}.
\tag{11}
$$

每个 nested $I_r^x$ 使用同一个真实右锚。完整新积分结束后才在左 collar 置外部 compact jets 为零；左多项式、ordered 字和真实常数全部保留。

若完整左式只余单字常数，则按原 single-word 的负号得到完整 local quintic 密度 $L$。程序输出全部密度和 Euler 项，使用真 compact 边界

$$
5\int L=\int u\,\mathrm{Euler}(L)
\tag{12}
$$

判定普遍零。Euler 非零只在完整局部化已成时给普遍非零；任何多字或非恒左多项式残余都完整输出并标 unresolved。没有有限 profile 代替普遍结论，也不对两函数另做秩实验。

## 8. 执行绑定与费用

新文件：

- scripts/literature_kk_minus4_natural_flux.py；
- computations/request-kk-minus4-natural-flux.json；
- .github/workflows/visible-kk-minus4-natural-flux.yml。

统一入口参数为 --request PATH --out PATH。Python 3.12.14，纯标准库，不安装新的符号或数值依赖。

workflow 先调用已付规则 reader，真实 pull public/private 并核双 README 精确差；再 detach 到触发请求的 source commit。请求绑定全部 38 个 source SHA，包括新 entry 和薄 workflow。实际 request bytes/hash、所有 source hashes、原输入与目标计划均进公开日志。private 凭据在规则读取完成后从环境删除；不打印凭据。

本次新增仅为两个目标的必要完整 self 装配、其势外槽收缩、两次五次通量映射和全部局部时的 Euler。typed hash 相同的势外槽跨目标共用缓存，实际新装配数量如实报告。

不执行 k0 锚，不运行 HH4 两个旧目标，不执行 R406 八 checks，不新增重复人工套件，不重 pure/rank/forcing/N0/N2/旧响应 producer，也不重建完整任意角 mixed 函数。

资源继承 frozen mapper：120 秒、512 MiB、8192-bit 有理数、100000 terms、300000 IBP calls、250000 cache entries；完整 report 上限 95000 bytes。到限或接口失败，报告真实 finite-fail 与完成阶段，不把未付项置零。没有事先声明 B/C 为零、局部或 S 整除。

原输入只在 runner 内存读取，输出 JSON/完整公式只留临时文件并打印原公开日志。不上传 artifacts、Release，不把可重算 payload 提交 Git，也不为原输出创建 blob。持久化范围仅人类稿、源码、设计、请求和必要身份元数据。

## 9. 后续数学范围

本设计尚未执行。即使 $B,C$ 都得到非零 local C² 密度，也必须在同一个最终母库及其完整共同正仿射/ordered 查询中判断其作用。

若两个完整密度落已付 Q4 的下降像，可用原同权 $E(U_{-4})=E(R_{-4})$ 精确支付 $E$ 分量后，才消去相应下降字符。

另一条条件性接口是 [R424](../results/R424-conditional-local-C2-minus4-functions-and-common-moment-fibers.md)：仅在完整局部性、五次、真实权和 C² polynomial 前提全部成立时，可从构造起点选择共同 $F^\star=(F_{\mathrm{rat}},D,E_5,M_{25})$，将全六类密度降到共同 Q4 头像。不能在已冻结母库上事后暗加 $M_{25}$，更不能由程序输出 universal 非零直接推正字符。

两目标的原 machine 字段“完整负四 Q2 字符或 actual joint 已解决”继续保持 false；任何理论推论另作人类证明。完整同路径 joint、period 和主课题完成均不在本次运行的自动结论内。
