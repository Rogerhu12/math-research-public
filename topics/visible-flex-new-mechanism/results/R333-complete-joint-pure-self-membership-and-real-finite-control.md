# R333：剩余两条权零联合成员身份与 whole-pure、完整 universal self 的真实有限同时控制

日期：2026-11-15。**公开实际结果与其严格数学后果。** 新科学只在 GitHub Actions run \(\mathbf{43740129876}\)、job \(\mathbf{132891272196}\) 执行；本稿仅消费其原日志、主报告和来源回执。没有在本地执行旧根评价、人工检查、求积或消元。

本次两条新目标均为 **MEMBER**。准确得到
\[
E(U_0)=E(\mathcal R_0),\qquad
\bigl(E(U)/E(\mathcal R)\bigr)_0=0,
\quad E=(\pi,\mathcal Q).
\tag{1}
\]
结合 R323 已付的整个联合闭锥满与 R206/R212 的真实有限实现，现可升级为
\[
\boxed{E(\mathcal S)=E(U).}
\tag{2}
\]
也就是说，任意**相容的整对 universal pure 与完整 universal self**，都由一条有限真实、同端口、\(M=\mathbf T=0\) 的路径准确实现；紧目标集具有真实有限 \(C^1\) 截面。

式 (1) 只在权零断言响应像等号。本文**没有**从它推出全权 \(E(U)=E(\mathcal R)\)。式 (2) 支付的是真实联合投影，不是完整 canonical 成本、固定圆的整个 mixed period 或同一 gauge 下的 fourth ruling。

主要来源：[R196](R196-complete-weight-zero-character-head-positive-ray-and-strict-canonical-cost.md)、[R201](R201-weight-zero-pure-image-and-failure-of-positive-character-readout.md)、[R206](R206-full-pure-cone-equivalent-to-actual-finite-pure-controllability.md)、[R212](R212-C1-sections-for-complete-real-pure-cost-control.md)、[R314](R314-ordered-matrix-defect-localization-and-faithful-Euler-self-coordinates.md)、[R316](R316-complete-weight-zero-self-membership-and-positive-character-representative.md)、[R322](R322-full-self-scaling-shift-and-exact-reduction-to-the-matching-response-weight.md)、[R323](R323-full-pure-self-cone-and-complete-negative-weight-response-control.md)。新设计与可复现参数见 [R329 两目标设计](../notes/weight-zero-joint-self-completion-design-20261115.md) 和本次固定 source 的 continuation request。

## 1. 空间、编号及本次真正的新目标

沿用真实完整 canonical 成本空间 \(U\)、完整响应空间 \(\mathcal R\)、universal pure 投影 \(\pi\)，并定义
\[
\mathfrak q_u(V)=\frac14[x^2]_{\rm left}V(u\odot u,0),
\qquad
\mathcal Q(V):u\longmapsto\mathfrak q_u(V).
\tag{3}
\]
这里 \(u\) 是同一合法区间内具有共同双零 collar 的任意实紧 profile；全部算子与积分保原共同右锚。\(\mathcal Q\) 是整个实际函数，不是某个母包、若干平移点或最高 jet 主项。

设
\[
\mathcal S=\{V_B:B\text{ 为有限真实同 scalar/frame 端口路径},
\ M_B=\mathbf T_B=0\}.
\tag{4}
\]
粗体 \(\mathbf T_B\) 是第三算子；\(\mathsf T(V)\) 是 R314 的有序三矩矩阵，两者不混用。先不要求单路径的空间末位移为零，后文闭 hook 推论另外使用真实 Klein 闭合。

R196 的完整真函数核给
\[
\dim U_0=19,\qquad
\dim\mathcal R_0=16,\qquad
U_0=\mathcal R_0\oplus
\operatorname{span}\{C_2,C_4,C_6\}.
\tag{5}
\]
\(C_i\) 是 R196 的八矩归一化 \(F_0\) 原系数，采用原 normal index：
\[
C_4:\ (h,k,\omega,\log h)\text{ 指数 }(0,4,0,0),
\qquad
C_6:\ (1,1,1,0).
\tag{6}
\]
这两个索引不是任意新取的坐标，也不是把 \(\omega\) 或 \(\log h\) 删除后的代入。

下文所有 \(R_j\) **一律是 R126 的原 old 列号**。本次完整十六列原顺序为
\[
0,1,2,3,4,5,7,8,9,10,11,12,13,15,17,19.
\tag{7}
\]
任何 \(R_7\) 或 \(R_9\) 都不得解释为 (7) 的紧缩位置。本文最终出现的六条响应的原语身份为：

| R126 old 列号 \(j\) | 原二次方向 | 原 \(W\) index |
|---:|---|---:|
| 2 | \(p_1\) | 1 |
| 3 | \(p_1\) | 12 |
| 4 | \(p_1\) | 16 |
| 5 | \(p_1\) | 35 |
| 7 | \(p_2\) | 6 |
| 9 | \(p_2\) | 14 |

\(C_2\) 的完整联合门已在 R316 付清。本次不重新评价它，也不重算原十三条 pure 核的 self。

## 2. 准确的两条新联合成员身份

本次得到
\[
\boxed{\begin{aligned}
E(C_4)={}&-\frac{95}{768}E(R_2)
-\frac1{3072}E(R_3)
-\frac{95}{1536}E(R_4)
+\frac{115}{768}E(R_5)\\
&+\frac1{64}E(R_7)-\frac{29}{1024}E(R_9),
\end{aligned}}
\tag{8}
\]
以及
\[
\boxed{
E(C_6)=\frac5{384}E(R_2)-\frac5{1536}E(R_3)
+\frac5{768}E(R_4)-\frac1{384}E(R_5)
-\frac1{512}E(R_9).
}
\tag{9}
\]
这些都是完整 universal pure 与完整 universal self 的**同一个响应组合**。不是分别为两个投影选不相容的代表。

等价地，定义真实成本空间中的
\[
\begin{aligned}
J_4={}&C_4+\frac{95}{768}R_2+\frac1{3072}R_3
+\frac{95}{1536}R_4-\frac{115}{768}R_5\\
&-\frac1{64}R_7+\frac{29}{1024}R_9,\\[1mm]
J_6={}&C_6-\frac5{384}R_2+\frac5{1536}R_3
-\frac5{768}R_4+\frac1{384}R_5+\frac1{512}R_9 .
\end{aligned}
\tag{10}
\]
则
\[
\boxed{\pi J_4=\pi J_6=0,\qquad
\mathcal Q(J_4)=\mathcal Q(J_6)=0.}
\tag{11}
\]
这里没有断言 \(J_4,J_6\) 的完整 mixed 函数为零，也没有把某个带负系数的线性组合直接称为实际负路径。

### 2.1 先读旧 pure 坐标，不重做 pure 原式

R201 已证明 \(\pi U_0=\pi\mathcal R_0\) 且该空间真维三；R116 的三条查询
\[
(c,r)=(0,32),(1,31),(2,30)
\tag{12}
\]
在该空间上是同构。本次直接读取 R124 同一 \(\Gamma\) 归一化完整 packet 与 R116 已存响应列的 (12)，得到
\[
\begin{aligned}
\pi C_4&=\frac1{48}\pi R_0-\frac1{64}\pi R_2-\frac1{96}\pi R_3,\\
\pi C_6&=\frac1{32}\pi R_2-\frac1{48}\pi R_3.
\end{aligned}
\tag{13}
\]
每条 (12) 的总幂 \(c+r=32\) 正确选择成本真权零。这里的函数身份使用已经发表的三维性与查询同构；不是以单个 pure 尾猜整个 universal identity。

因此两个新的 pure-zero self 目标为
\[
A_4=C_4-\frac1{48}R_0+\frac1{64}R_2+\frac1{96}R_3,\qquad
A_6=C_6-\frac1{32}R_2+\frac1{48}R_3.
\tag{14}
\]
没有恢复任何 pure 原根，没有新 profile 评价，也没有新 pure word normalization。

### 2.2 只消费已完成的十三列 full-self 比较空间

R316 已把整个 \(\mathcal R_0\cap\ker\pi\) 的十三条分支输出为完整 \(\mathsf T\) 与 Euler 坐标，其 self 像真秩为七。本次在 runner 内存只读原 run/job 的完整日志；原 61,441B 主报告确实保存了十三列，故不用重新映射它们。

本次成员表达只涉及原标签 \(4,5,7,9\) 的四条 pure 核：
\[
\begin{aligned}
K_4&=R_4-R_2+2R_3,\\
K_5&=R_5+\frac14R_3,\\
K_7&=R_7-\frac43R_0+\frac43R_3,\\
K_9&=R_9+6R_2-\frac83R_3 .
\end{aligned}
\tag{15}
\]
真实新 self 解为
\[
\begin{aligned}
\mathcal Q(A_4)
&=-\frac{95}{1536}\mathcal Q(K_4)
+\frac{115}{768}\mathcal Q(K_5)
+\frac1{64}\mathcal Q(K_7)
-\frac{29}{1024}\mathcal Q(K_9),\\
\mathcal Q(A_6)
&=\frac5{768}\mathcal Q(K_4)
-\frac1{384}\mathcal Q(K_5)
-\frac1{512}\mathcal Q(K_9).
\end{aligned}
\tag{16}
\]
将 (13) 与 (15) 代回 (16)，正是 (8)–(9)。程序还按原标签独立重建了 (10)，避免紧缩列号导致另一条形式关系。

### 2.3 新目标本身并非 self 零

两个新映射的成本权均为零，所观测 self 权均为 \(-2\)。R314 给出的真实结构是
\[
\mathfrak q_u(A_i)
=\mathcal N_{\mathsf T(A_i)}(u)
+\int L_i(x,u,u',u'',u''')\,dx .
\tag{17}
\]
原尾、嵌套积分增量、左端常数均保留；局部密度和 Euler 多项式逐项输出。

| 新目标 | 原 mixed 项数 | diagonal 项数 | whole word 项数 | self word 项数 | 非零完整坐标数 |
|---|---:|---:|---:|---:|---:|
| \(A_4\) | 2,433 | 186 | 62 | 17 | 37 |
| \(A_6\) | 2,244 | 170 | 57 | 13 | 36 |

其中
\[
\mathsf T(A_4)_{22}=-\frac1{1536},
\quad\text{其余八项为零};\qquad
\mathsf T(A_6)=0.
\tag{18}
\]
两者完整 Euler 多项式都非零。因此 MEMBER 不是因为目标原来就零。37/36 是本次目标的非零坐标记录数，不能称为函数空间维数。

## 3. fresh 原复合验证及零判据

成员求解结束后，程序没有只核保存坐标的残差。它从同一原 mixed 根与原响应根重新组成 (10)，各启一个独立 mapper，重新作完整 self 提取、九个有序尾核、局部化与 Euler 计算。

| 验证 | \(J_4\) | \(J_6\) |
|---|---:|---:|
| fresh 原 mixed 差项数 | 2,492 | 2,198 |
| 九个真实 \(\mathsf T\) 坐标 | 全零 | 全零 |
| 完整 Euler 坐标 | 全零 | 全零 |
| whole word 与 \(\mathsf T+\int L\) 重构差 | 准确零 | 准确零 |
| 实际 self word 余项数 | 0 | 0 |
| 新 primitive calls | 184 | 124 |
| cycle fallback | 0 | 0 |

完整 self 的充分且必要判据来自 R314 的忠实 \(\mathsf T\)/Euler 呈示。**一般 positive case 不额外要求某个 sound NF 必须字面零。** 本次两条 fresh 差碰巧还得到 self word 字面零，这作为实际更强观察保留，不能反过来把它当作一般成员门的必需条件。

相关原式身份为：

| 身份 | SHA256 |
|---|---|
| \(A_4\) 原 mixed | c6f717ee84879b3bb6c463369ef0438854de33993a091aae5277eb2f1ae48a38 |
| \(A_6\) 原 mixed | b20ee73c23496e83e9567a3e7f5099965eda9a769aa3a04b0abffa2164a8fa44 |
| \(A_4\) faithful \(\mathsf T\)/Euler 坐标 | 093ba29b33dc4eb44976756e838f1f1758f697e5c57cfbd717e28622759e6ca8 |
| \(A_6\) faithful \(\mathsf T\)/Euler 坐标 | 338638db3e1121d4e6dc7a675db9f78d7313a1564752e20964ce726055715756 |
| \(J_4\) fresh 原 mixed 差 | b2a085ad289968fdf2cb6b0df466fcb3ca643f56d6b3106dc322d01b570f2b81 |
| \(J_6\) fresh 原 mixed 差 | 432254370e395477f7636d7f16348a4d3467ffd11b8189a8d249ec813596724e |
| \(J_4\) fresh diagonal | dafd2752120f13e070871fc280e319e610e8d96036efbf116d9e91e7d9237686 |
| \(J_6\) fresh diagonal | 163cb66d73959b8db6023525e5cb07755346950b7a4b8d7cb5ec9c17c16a74dd |
| \(J_4\) whole word | 98b25b18bbafca3bae2f3f3ce735accc01ee6f82a9cf76c5d1c25663c3811da3 |
| \(J_6\) whole word | 90f7069739089e4f438ad82d15b8787693de430b4d79fa11af9ea808f2fc34df |
| 两条空 self word 列表 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |

哈希标识被消费的原件；真正的数学零证是上述完整原式重构及 R314 的忠实性，不是哈希相等本身。

## 4. 权零联合像和核的严格维数后果

R316 已给
\[
E(C_2)\in E(\mathcal R_0).
\tag{19}
\]
将 (8)–(9) 与 (5)、(19) 合并，即得 (1)。这没有重新做完整 H0 的 rank 实验。

还可从已付维数准确推出：
\[
\boxed{
\dim E(U_0)=\dim E(\mathcal R_0)=3+7=10,
}
\tag{20}
\]
\[
\boxed{
\dim(U_0\cap\ker E)=9,\qquad
\dim(\mathcal R_0\cap\ker E)=6 .
}
\tag{21}
\]
理由是 \(E(\mathcal R_0)\to\pi\mathcal R_0\) 的满射有核
\(\{0\}\oplus\mathcal Q(\mathcal R_0\cap\ker\pi)\)；前者目标维三、后者维七。再用 (5) 和秩零度定理即可。这里的“七”仍是 R316 的旧真秩，不冒为本次重新取得的科学结果。

R316 的 \(H_*\) 与本文 \(J_4,J_6\) 都在 \(\ker E\)，且其模 \(\mathcal R_0\) 的类分别是 (5) 的 \(C_2,C_4,C_6\)。因此它们给
\[
(U_0\cap\ker E)/(\mathcal R_0\cap\ker E)
\]
的三个独立类。没有因此断言它们属于完整响应空间。

特别，R316 已付的
\[
\lambda_+(H_*)=1,\qquad E(H_*)=0
\tag{22}
\]
保持不变。完整正字符不经整个 \(E\) 下降；更强的联合控制与该正字符没有矛盾。

## 5. 从已满闭锥升级到真实有限联合半群

这一节把实际 MEMBER 用于既有真实构造，明确不是把 signed span 当作路径。

### 5.1 准确商空间与可逆缩放

记
\[
\mathscr P=E(U),\qquad
\mathscr L=E(\mathcal R),\qquad
\mathscr C=\mathscr P/\mathscr L,\qquad
q:\mathscr P\to\mathscr C.
\tag{23}
\]
R322/R323 已付 \(\ker E\) 和 \(\mathscr L\) 的仿射稳定性，所有有限 Laurent 投影仍在同一真实函数空间。本次 (1) 正是
\[
\mathscr C_0=0.
\tag{24}
\]
故正缩放的生成元 \(D\) 在 \(\mathscr C\) 上可逆：其有限整权分解没有零权。这不要求其他权的 \(\mathscr C_\sigma\) 为零。

R323 已独立证明
\[
\overline{\operatorname{cone}(E\mathcal S)}=\mathscr P.
\tag{25}
\]
原证明逐项排除了可能正仿射字符，保 \(\lambda_+\) 在 \(H_*\) 上的非零值。式 (25) 是完整联合像的满闭锥，不能直接删去闭包。

### 5.2 真实商截面：有限 floor 复制，保全部桥成本

对 (23) 直接应用 R206 已付构造。由 (25) 选有限个实际
\(M=\mathbf T=0\) 路径 \(B_i\)，使 \(qE(V_{B_i})\) 正张成整个商，并取严格正配平
\[
\alpha_i>0,\qquad
\sum_i\alpha_iqE(V_{B_i})=0.
\tag{26}
\]
只把 \(\alpha_i\) 用来选整数 \(n_i(N)=\lfloor N\alpha_i\rfloor\)，不使用实次数路径复制。

每个 \(B_i\) 作 \(H=e^{t_i}>0\) 的真实几何缩放，使用 R70 同端口桥及其真倒行修复端口。M、第三历史和全部桥第四成本按原公式保留。商成本为
\[
\sum_i n_i(N)e^{t_iD}qE(V_{B_i})+\mathcal E_{\mathscr C}(t),
\tag{27}
\]
其中桥项是与 \(N\) 无关的固定 \(C^1\) 函数。

由 \(D\) 可逆，可选 \(\dim\mathscr C\) 个参数，使 (27) 除以 \(N\) 后在零点的极限导数可逆。R206 的统一收缩论证给：对任意紧商目标集，选一个有限 \(N\)，有同一真实有限词、\(C^1\) 依赖目标的准确商截面。所有缩放只在 \(H=1\) 附近固定开区间内，端口与共同 scalar 包络不随之后的复制数扩大。

### 5.3 先付响应 prototype 的商基准，再付整个响应分量

选有限真实响应 \(K_j\)，使 \(E(K_j)\) 是 \(\mathscr L\) 的基。它们的真实第三 prototypes \(L_j\) 可能有非零第三算子，但各原成本仍属于 \(U\)：实际 \(L_jL_j^{\rm rev}\) 的 \(M,\mathbf T\) 为零且第四成本为 \(2V_{L_j}\)。这只证明线性空间归属，未使用“半条路径”。

用上一商截面先给每个 \(L_j\) 接一个真实 \(M=\mathbf T=0\) 校正，使其商成本准确零；完整第三算子及响应 \(K_j\) 不变。新增校正的整个第四成本保留在新的 prototype 基准中。

R101 真实复制字随后有准确联合成本
\[
E_0(t)+n\left(2\sum_jE(\widehat V_j)+\sum_jt_jE(K_j)\right).
\tag{28}
\]
括号内基准的商为零。因此 (28) 的商只剩 \(qE_0(t)\)，与最后响应复制数 \(n\) 无关。对给定紧目标集，再用一个已经固定的商截面准确付掉这个 \(t\)-依赖商误差，保其全部响应分量。

最后响应坐标成为
\[
F(p,t)+n(A+t),
\tag{29}
\]
其中 \(F\) 在所选紧参数盒中 \(C^1\)，且是在选 \(n\) 前固定的完整函数。选一个有限大 \(n\)，使
\[
t\longmapsto -A+n^{-1}\bigl(p_{\mathscr L}-F(p,t)\bigr)
\]
为统一近恒等收缩。R212 的加强给准确解及其 \(C^1\) 目标依赖。两个商校正的基准、真实桥与复制成本都在 (27)–(29) 内；没有遗漏未知成本再用形式响应消掉它。

这里用到的 \(C^1\) 性不是由抽象有限维自动推出：pure 原函数查询与完整 self 的 profile 评价在 \(\mathscr P=E(U)\) 上共同分离，故可选有限个这样的真实评价作为坐标。其关于固定有限路径参数的导数来自原 R56 恢复、有限积分与 Duhamel/分部积分公式，连同 R70 的真实参数桥给 (27)–(29) 的 \(C^1\) 依赖。没有声称 self 评价单独分离整个 \(U\)。

于是严格得到 (2)。这套论证也覆盖 \(\mathscr C=0\) 或 \(\mathscr L=0\) 的退化情形，分别直接使用响应或商截面。

### 5.4 同时控制的准确含义与闭 hook 推论

目标是任意 \((p,q_{\rm self})\in E(U)\)，不是不加相容限制的
\(\pi U\times\mathcal Q(U)\)。对每个这种目标，存在有限真实路径给整个函数身份
\[
\pi V_B=p,\qquad
\mathcal Q(V_B)=q_{\rm self}.
\tag{30}
\]
特别可取零目标。此时 \(\pi V_B=0\)，R314 的忠实性再给
\[
\mathsf T(V_B)=0,\qquad
\mathfrak q_u(V_B)=0
\quad\text{对全部合法实紧 }u.
\tag{31}
\]
这已超出固定母包的有限 self 查询与 R323 原先的十个负权坐标。

若按 R206/R121 从起点加入固定真实第三 hook 背景及全部闭合桥，Klein 闭合的完整成本是 \(V_{\rm base}+4V_B\)。取
\[
E(V_B)=-\frac14E(V_{\rm base})
\]
即可得到空间闭合、保同一非零第三 hook 的有限真实几何，满足 whole-pure 和整个 universal self 同时为零。所有目标与基准在同一联合投影下支付。

本结论不预给统一长度、任意窄指定 I、reach、导数盒或原某条已固定 Gaussian/Morse 几何。共同合法区间在有限 prototype、桥与紧参数包络固定后选择。若还要保另一个观测系统或指定 germ，须按对应增强 IFT 的真实接口从起点共同安装；不能因这里有 \(C^1\) 截面就静默保留额外约束。

## 6. 完整 mixed 与 fullperiod 仍保留的门

R159 对 pure-zero 成本给唯一 balanced 双线性表达。对固定合法 \(f,g\)，两个完整 mixed 目标仍是
\[
D_V=B_V(f^2,f^2)-B_V(f^2,g^2),\qquad
G_V=B_V(f^2,f\odot g),
\tag{32}
\]
并且
\[
V_\theta=\sin^2\theta\,D_V-\sin(2\theta)\,G_V.
\tag{33}
\]
完整 self 零只杀掉 (3) 的整个左二次系数泛函，并由 R314 付有序尾矩；它不把 (32) 这两个完整输出函数置零。

因此本次仍没有支付 R225 的全部平台函数、内部退化、端点 germ、通量及同右锚积分常数，更没有证明同一二阶 gauge 还满足全部 fourth ruling。任何新增 \(\int u'''V(u^2,0)\) 型 period 观测也须用它自己的原式证明，不能从 (3) 的零值推得。

尤其 (22) 与 R196 对每条非空实际零矩路径的严格正性
\[
\lambda_+(V_B)=L_B+\int(h_s/h)^2ds>0
\tag{34}
\]
仍成立。故 signed **whole canonical 成本**的任意实现依然不可能；真正可任意实现的是本文精确定义的联合投影。本文没有把固定圆代入或 gauge 商自动等同于该联合投影。

## 7. 新执行与必要输入恢复的分账

本次只作两个新完整 self 目标和两条 positive fresh 原差。明确执行范围：

| 项目 | 实际数量/范围 |
|---|---|
| 新完整 self 目标 | 2：\(A_4,A_6\) |
| 已存 full-self 比较列只读 | 13 |
| 旧十三列 self 重新映射 | 0 |
| 旧 Euler 多项式重算 | 0 |
| 旧完整 H0/响应秩实验 | 0 |
| 已存 faithful 坐标的一次分解 | 1；用于两个新 RHS |
| 新 RHS 求解 | 2 |
| 必要旧 mixed 响应原根恢复 | 16；逐根核 R126 原 SHA |
| 必要旧 static mixed 目标根恢复 | 2；逐根核 R196 原 SHA |
| pure 原根恢复 | 0 |
| 新 pure normalization/profile evaluation | 0 / 0 |
| 新 \(N\) 响应或旧 3974 forcing 重编 | 0 / 0 |
| 新目标共享 mapper primitive calls | 160 |
| 两 fresh mapper primitive calls | 184 / 124 |
| 全部本次新 primitive calls | 468 |
| 各 mapper cycle fallback | 0 |

原 R126 没有 portable 响应 DAG，后来 metadata-only 运行也未保存那些原根，所以必要恢复十六条 mixed 输入一次。该恢复不重作旧 pure 映射、旧 self 坐标、原 profile 评价或旧秩实验。

两个 static 输入仅为本次所需的原 \(\Gamma\) 组合与真权投影，不重新编译整个 head；原 \(C_2\) 及其余 head 根没有恢复。

## 8. 八项新开发检查及实际资源

本次公开首验八项均通过；没有在本地执行：

1. 原 COMPLETE_REPORT 的 BOM/时间戳 framing、精确原 JSON+换行哈希，以及重复/篡改拒绝；
2. 保存的完整 \(\mathsf T\)/Euler 列读取和 SHA 绑定，不新作 Euler；
3. 同 \(\Gamma\) 完整 packet 的三条 degree32 坐标读取及准确缺零 packet 语义；
4. 两个 pure RHS 的原三基坐标转换；
5. 一次保存列分解、非单调 pivot、两个 RHS 的成员/faithful 分离人工情形；
6. pure 核位置到 R126 old 标签的复合；
7. 原 job 日志的 fake redirect 不转发 API credential，人工不联网；
8. 旧递归 source 叶与原 receipt 的绑定及不匹配拒绝。

| 阶段 | elapsed seconds | peak RSS MiB |
|---|---:|---:|
| 八项新开发检查 | 0.004333594000001995 | 32.89453125 |
| 两目标与 fresh 实际 | 6.521884228999994 | 115.6484375 |

原 R316 job 日志在 runner 内存读取，报告的该读取耗时为
0.4073396200000019 秒；没有重跑旧开发或研究。

literal.Budget 被监测部分为 **703 operations、最大 40 integer bits**。这不是全部原 DAG 恢复、Fraction 运算或全部 468 primitive 内部操作的总量/最大位数，不作这种外推。

声明的实际上限保原设计：240 秒、1024 MiB、8192 integer bits、100000 terms、300000 IBP calls、250000 cache entries、95000B 主摘要和 4000000B 临时 proof。主报告记录的科学状态是 complete，两目标都完成；没有把预算/输出截断当作零。

## 9. 本次与旧输入的可复现身份

### 9.1 本次公共运行与临时输出

| 项目 | 准确身份 |
|---|---|
| public run | [43740129876](https://github.com/Rogerhu12/math-research-public/actions/runs/43740129876) |
| science job | [132891272196](https://github.com/Rogerhu12/math-research-public/actions/runs/43740129876/job/132891272196) |
| source commit | a5383f62d353890cc24e927b669dd2d6b67f8c78 |
| lane | weight_zero_joint_self_completion |
| schema | visible-flex-weight-zero-C4-C6-complete-self-v1 |
| 新 driver | literature_weight_zero_joint_self_completion.py；50185B；1f5d671598ca6fc4a804c6f22a65d145b5ced3743506a2144d507717ff4789d3 |
| 已审设计 | weight-zero-joint-self-completion-design-20261115.md；17493B；ce64a826558ac62eab9c371e1fc4a12dd38a7dd9fef0f3d1c02106f515877c0a |
| request | request-continuation.json；10300B；21bc20e376cf894d5d699d8777330f3e80ee906b719335770ead87634d2f4da6 |
| 主报告 | weight-zero-joint-self-completion.json；37516B；d4c5709c150392118ea0189be0f2114e52e9511df12d90f139836cace3863ca3 |
| 新开发报告 | weight-zero-joint-self-completion-development.json；9773B；97bd75fa11dd55a2cf5b7a6c854bd67655d988c00944c7d28b562e92b3794489 |
| 仅 runner 内存 proof | 30124B；9b11f5b8d76d4bf3c8fd7bb5e60a96707a1fe50ffe014ebc668a611c928e59e9 |
| 已发布来源 receipt | 56025B；2854aecf26a0abf3b013d0674965315a3ba1702c681b76cf7f9ba1ba32947004 |

来源回执为
[notes/actions-43740129876-1-weight_zero_joint_self_completion/receipt.json](../notes/actions-43740129876-1-weight_zero_joint_self_completion/receipt.json)。

对原 stdout 的两条完整 JSON 报告加原换行重新核 SHA，均与 receipt 的 bytes/SHA 完全一致。request 的 34 个直接 source bindings 全部匹配 receipt；主报告 source_hashes 中 46 个递归叶记录、29 个不同科学源码名也逐项匹配，无冲突。receipt 的 262 项 source inventory 不等于本次执行了 262 份程序。

research 之前实际 public pull/read 完成于日志
2026-11-15T17:16:32.9262082Z，读取 commit
96744db0bc1fed0826fa0999cb0b7eee7ddb1d62，随后恢复上述固定计算 source。publisher 最后实际 pull/read 为
9d548f3ed9ed870b3b4f94851391521d99be4b32，双 README 未变。公开仅存元数据、人类说明和源码参数；可重算输出与 proof 没有写入仓库、Release 或 artifact。

### 9.2 两个原 static 根

| normal index | 真权零 mixed \(-2\) 原 SHA | 原项数 |
|---:|---|---:|
| 4 | 1d67672bb734f602675f84768b8afd62363d3742ca203ea01b23c9b1f3f0b592 | 1461 |
| 6 | 5ca598f50107cf8f059608f27694ad87bb5cbd26be152ff18d8d0f2e2a95bc02 | 1321 |

同一参考数据 \(\Gamma\) 的 SHA 为
c6276335dd47380509870798123478dc1b5a25ad83f3eef15d30cedcef4ece0b。
两根与 R196 run43681388902/source7872857e7750e1b5091560b6362e52dd952bc6fa 原 25121B 主报告
838266c7b4b86b137482127e7e874d8d3eb014aa5745b9be6fceb2d9d3dc7fa4
匹配。C6 的未投影 \(\Gamma\) 原组合还保
245f99b72915054cbaa798b099dd4b343dbf80f8b45b3c09d1b658ee548be024；
不把它与投影后真权根的 SHA 混同。

### 9.3 原比较列与 pure 数据

R316 比较来自：

- run43735872441，job132878270740，sourceca186db057ed753abe565d0c3c2c8305278b5af7；
- 完整原主报告 61441B，SHA731ffae43cc8f06346801c444a7de010fe2cf6f9f05ecf4b650d319fa2ee06fd；
- 原 receipt 55780B，SHA8d79ddda157153788ae70bb1cc44d6c64d4672541bb2e66f7cfbaf33f9549701；
- 原 job 日志 182877B，SHA4d658489abd694f9f4cde2204aec9d23dc507d9ebae47168e42123cf4ff1288f；
- 只读十三 faithful 列的规范坐标 SHA07e7d6c2fb24279e47ea6e2f48eb37e112099e20b4b183e2c12efe0ce70c679e。

原报告确含完整十三列，不是只保存 rank7 或 hash。读取时核 45 条旧 source 记录；原日志只在 runner 内存使用。

pure 坐标只读 R124 run43649160345 的完整同 \(\Gamma\) normalized-static packet：
57845B gzip/022cd4f767d40b5ad21089e4cf88f7f6d4e6e051b7d730c038e87ab0e0961175，
raw489034B/ced7357546b2c85610cf200e961c4e568a7a8f53407bf8da033eee8b9cb86ed7；
以及 R116 run43646543691 的原三查询列：
44576B gzip/b0859868f2db2a08ca1b2831e5ab010840eed8e7ebda01fca49d598822d147a4，
raw274274B/a8b5577903e419d2eabe2c327c2c721401acea2d0845017f86c260b2ddb8c36c。
这些数据是必要旧输入，未进行新 profile 评价。

其余原 static/W 与 R126 来源均由本次主报告 inputs 完整绑定。原 static producer 的旧 completion 是 output_limit；本次仅使用它已明确完整导出的 W/static 原根与匹配 SHA，不把旧状态改成 complete。

## 10. 后继唯一有用的范围

本稿已将 R323 的条件性“全 pure+全 self 实际有限实现”变成无待定成员门的结论。今后需要 pure/self 零背景时，可以直接消费 (30)–(31)，不再重复 C2、C4、C6、旧十三列、rank7、pure19 或整个 3974 forcing。

后继仍须处理相应合法 profile 圆上**同一元素**的两个完整 mixed/cross 函数与 fullperiod/ruling 相容条件。若要保已安装的局部几何、Morse 性或其他 finite observations，须使用其完整增强控制接口，不把多个分开可控系统直接相加为联合满射。

作者责任：本稿准确区分已发表数学、公开首实际、旧输入恢复、保存坐标复用和纸面实际构造。原式系数全部采用 R126 old 标签；全部成本历史、基准、共同右锚和真实端口义务保留。既未把非零 NF 当非成员，也未把闭锥或 signed span 当作已构造路径。
