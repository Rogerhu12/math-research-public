# R133：完整 5970 格的同一传播子与方向矩阵数据合同

## D.1　对象和已有结果

本消费者固定原物理 $\eta_0,\nu$ 与 continuous repaired M32 背景，只处理原 $[0,9/10]$ 的完整 finite193 压缩体。193 槽为 96 个 odd 非均值与 97 个 even（包含独立均值）；原加权未知量 $y=R(r)h$ 和完整 $R'R^{-1}$ 不变。高输入保留 $97\le |j|\le160$ 的 128 个真实反射方向，跨块输出精确落在 $33\le |j|\le96$ 的 128 槽。这里只构造后续矩阵双扫所需的完整局部数据；不能从覆盖直接宣布完整方向 Green 或无限 PDE 逆。

固定原 complete profile：

- 原 5970 格 native SHA256：3460a4b5636bf6a3d9c160f6141ab5153fc5fc705ca79000c5f10370a978cb69。
- 原 artifact process SHA256：16608b57571d17a427857bcfe0127186589b3f79e93d89a7e423ac48a2740af9。
- 原 16 份 full-reference native 与 16 份 Q-slice 都来自公开 run 43594139132。完整 profile 已逐行保存原 full row 的 canonical JSON SHA；新消费者再次对全行绑定，不能仅比较区间或样本。
- 原 interval model SHA256：b30eb7299d5803856712134947f3d7899961cc3ab7597ce961b9bf0cf5205183。
- 原 validator SHA256：998e4112f4ee79706f43b9ac550fcb15023e0899999fa8516c7cec07c3a7ff97。

原 indices $0,76,3300,5969$ 的同一传播子、端口、全部源／输出 Gram 已在公开 run 43648579604 通过 15 门，其 native SHA256 为 9a46d9fc76499a17a90a0a153a0c4907415eadcedfd9f50f70fd82d08f9dbc7c。这四行及其科学数组、原始 artifact 身份逐字节复用，不重新计算。它们采用原独立记录的 dyadic $A,F$；新 5966 格采用以下 canonical exact 定义，二者各保完整模型差证书，不伪称同一种浮点选择。

## D.2　原精确系数与新径向方向

每个原闭格 $[l,r]$ 的精确参考为

$$
A_{\rm ref}(s)=\sum_{k=0}^{3}A_k s^k,\qquad
s=\frac{x-r}{l-r}.
\tag{D.1}
$$

这里 $A_k$ 由原记录的全部 physical 65 槽 cubic、intrinsic scalar cubic、完整 128 个 primitive 中间模和精确线性 $R$ 的规定截断定义。新源码只从这些已存字节和公式包围同一精确系数，不再求 target 或候选值，不借用未存的 BLAS 矩阵。Arb 的区间是同一 canonical 对象的包络，不能取其中点另立模型而不记费用。

原 validate_cell 源的
generator_reference_coefficient_operator_bounds 恰为 D.1 中四个 $A_k$ 的完整欧氏 operator 上界 $m_k$；入口同时逐字锁定原 recurrence 字符串，因此不会把 centered、Legendre 或相反坐标系的界直接拿来用。设 $h=r-l>0$，新正向变量 $t=(x-l)/h=1-s$。则

$$
\widetilde A_j=(-1)^j\sum_{k=j}^{3}\binom{k}{j}A_k,\qquad
a_j=\sum_{k=j}^{3}\binom{k}{j}m_k,\qquad
M=\sum_{k=0}^{3}m_k
\tag{D.2}
$$

分别给完整系数上界和全格 $\|A_{\rm ref}(t)\|\le M$。D.2 的 $M$ 可直接沿 $s\in[0,1]$ 取，不必把正向各系数绝对和再当更大的唯一全格界。

原两处完整 true-generator error 必须重叠且取其上端最大值 $E_{\rm old}$。重建函数产生的同一参考截断／舍入包络不再次收费；原 $E_{\rm old}$ 已包含真背景、原目标和所有径向弃项。全过程不会删除 mean-rank 或原 primitive 列。

## D.3　同一 $A_{\rm ref}$ 的未舍入 $F,C$

以精确递推定义

$$
F_0=C_0=I,\quad
F_{n+1}=\frac h{n+1}\sum_{j=0}^{\min(3,n)}\widetilde A_jF_{n-j},\quad
C_{n+1}=-\frac h{n+1}\sum_{j=0}^{\min(3,n)}C_{n-j}\widetilde A_j.
\tag{D.3}
$$

它们分别近似 $F_t=hA_{\rm ref}F$ 和右逆方程 $C_t=-hCA_{\rm ref}$。本次不对这些系数选择新的 dyadic 中点。令

$$
f_0=1,\qquad
f_{n+1}=\frac h{n+1}\sum_{j=0}^{\min(3,n)}a_jf_{n-j}.
\tag{D.4}
$$

非负有向上舍入递推给 $\|F_n\|,\|C_n\|\le f_n$。截到 degree $D$ 后，D.3 精确消去 $0,\ldots,D-1$ 次的微分残差；按真实径向 $x$ 的完整尾界为

$$
d_D=\sum_{k=D}^{D+3}\ \sum_{\substack{0\le j\le3\\0\le k-j\le D}}
a_j f_{k-j}.
\tag{D.5}
$$

因此两个未修补多项式均满足

$$
\sup\|F\|,\sup\|C\|
\le \min\!\left(\sum_{n=0}^{D}f_n,\ e^{hM}(1+h d_D)\right),\quad
\sigma_{\min}(F)\ge e^{-hM}-h e^{hM}d_D.
\tag{D.6}
$$

上述 $C$ 上界同样由右乘方程的变分常数公式成立。数值 D 在 $8,12,16,20,24,32,40,48,64$ 中取首个满足

$$
h e^{hM}d_D<2^{-52}e^{-hM}
\tag{D.7}
$$

的值。选阶也是本次公开 Actions 的新标量计算；若没有一个满足便明确失败并保已完成前缀，不把未验证的 degree64 强行接受。

## D.4　真正的完整三角端口

端点原 $Q_-,Q_+$ 是已存精确 dyadic $193\times96$ 矩阵。新的 97 列补空间选为实际 QR 输出，保存其字节、完整 Gram 和真逆证书，不假定另一硬件会产生同一补空间。令 $S_\pm=[Q_\pm,N_\pm]$。从 $S_+^{-1}F(1)S_-$ 选择完整 dyadic 上三角端口

$$
T=\begin{pmatrix}A&B\\0&D\end{pmatrix},
\quad
\Delta=S_+TS_-^{-1}-F(1),
\quad
\widehat F(t)=F(t)+t\Delta.
\tag{D.8}
$$

原 96 与 97 两个对角块的全逆均须实际核验。被删除的完整左下块和端口中点费用全部落在 $\Delta$，没有当成零误差。设 $\delta=\|\Delta\|$，则

$$
\sigma_*=\sigma_{\min}(F)-\delta>0,\qquad
d_* = d_D+(h^{-1}+M)\delta,\qquad
\|A_{\rm true}-\widehat F_x\widehat F^{-1}\|
\le E_{\rm old}+\frac{d_*}{\sigma_*}.
\tag{D.9}
$$

所有状态与后续源、输出 Gram 使用同一个 $\widehat F$。原另算的 backward 多项式不作为它的准确逆。

由 $(C\widehat F)'=(C'+CA_{\rm ref})\widehat F+
C(\widehat F'-A_{\rm ref}\widehat F)$ 得

$$
\|C\widehat F-I\|\le
h(d_D\|\widehat F\|_\infty+\|C\|_\infty d_*),\qquad
\|\widehat F^{-1}-C\|\le
\frac{h(d_D\|\widehat F\|_\infty+\|C\|_\infty d_*)}{\sigma_*}.
\tag{D.10}
$$

实际 gate 还要求第一项小于 $1/100$。它是同一传播子的后验逆包络，未推导全区逆。

## D.5　128 方向源与两个完整 Gram 通道

真实跨块为 $R P_{\le96}A_{\rm true}P_{97\ldots160}$，高输入以 ordinary pair 范数计，右侧没有 $R^{-1}$。固定 M32 背景使全部乘法差频至多 64，故输出只有 $33\ldots96$；常 meanrank 不跨块。高输入乘第一个 M32 系数后，中间模可能到 192，但要经第二个 M32 系数回到输出 $|j|\le96$，只读取 $|\ell|\le128$，所以原完整 128 个 primitive 中间模足够，正负反射槽均保留。

新 canonical 源 $B(t)$ 保原 cubic 截断后再乘完整线性 $R$ 的 degree4。其误差使用原 raw Wiener operator 费用的 $5/3$ 倍，再乘 $\max(1,\rho_l,\rho_r)$：角导的旧 $384$ 升为 $640$，零阶和 primitive 项维数无关，统一 $5/3$ 安全。此论证依赖原 Wiener 公式，不能用一个 finite Hilbert–Schmidt 上界作同样转授。

新格只需两个通道：$B$ 与 edge128 坐标嵌入 $E$。前者保实际跨块方向，后者单独支付 $B_{\rm true}-B$，二者同源不能声明独立。对任一通道，令 $P(t)=S_-^{-1}C(t)B(t)$，$\eta\ge\|S_-^{-1}(\widehat F^{-1}-C)B\|_\infty$。完整 signed Gram 满足

$$
H_{\rm true}\preceq
H_P+\left(2\eta\sqrt{h\,\operatorname{tr}H_P}+h\eta^2\right)I,
\quad
H_P=\int_l^r P P^*\,dx .
\tag{D.11}
$$

积分以完整 shifted Legendre 系数和真实 $dx$ 精确计算。保存对象为完整对称 dyadic midpoint 加已验证 exact dyadic $\lambda I$；对称上三角存储没有删去 $p/q$ 相关项或 mean。原四成功格的第三 edge_physical 通道原样保留，不能悄悄删除旧科学数据。

## D.6　输出和共享端点

保存同一 $\widehat F S_-$ 的加权输出 Gram 及 physical pair 输出 Gram。后者 odd 块权为 1，完整 even 块包括均值，以该真实闭格的正下界 $\rho_{\min}^{-2}$ 收费。固定负窗沿 $2383968743003/10^{13}$ 精确截取；位于其内的全格复用同一 physical 矩阵，位于其外为准确零，唯一相交格使用真子区间积分。没有把全区长度替作负区长度。

相邻格可以有不同 $N$，但入口必须核同字节 $Q$ 与同一物理端点 $R$。于是准确坐标事件

$$
C=(S_+)^{-1}S_-=
\begin{pmatrix}I&B_C\\0&D_C\end{pmatrix}
\tag{D.12}
$$

的左下块是代数上的准确零，$D_C$ 因全 $S_\pm$ 可逆而可逆。它是零长度的坐标改变，physical $y$ 连续，不产生新的物理跳。后续 $V$ 若独立选择 dyadic 中点，$Q\,\Delta V\,q$ 仍是真跳，必须使用已成逐接口冲量增益或更细完整相关核收费。D.12 不能免掉这种舍入。

## D.7　完整范围、保存和未付项

32 个互斥组各至多 192 个原 cell，准确排除四个已成功格，合计新 5966 格。plan 固定全部原 row hash、Q/R 接口和原成功身份；range 每完成一格原子保存 native、科学数组 SHA 与真实 run/attempt/artifact 来源。后续从失败发布或失败数学的真实成功前缀继续，不要求旧 process.complete 必须为真；但 complete native 复用必须有全部数学门和实际 child0。原始失败与前缀身份均保留。

大 F/C 系数不另存：新格的 exact 定义已由原 row、D.3、实际端口 $T,S_\pm$ 唯一决定。真正供后续矩阵双扫使用的全 $T,H,J,S$ 数组保留在公开 Actions artifact，每件含原字节和形状 hash；旧四格数组也只从其原 artifact 读取。缺失数组不能重建成“相同浮点字节”再伪称原件。

完整覆盖后仍需实际进行方向矩阵双扫，支付所有 $V$ 舍入跳、真实腰行与真帽 97 行偏差、body 模型差和跨块源误差。端点 $q_R=0$ 只是名义 regular 图；不能代替真正的帽 Robin 与独立 mean 行。既成有限193 Green 可用于后验恒等式的各缺陷，但不能把一个 ordinary 源常数用来吞掉边界或跳。未知高块返回、全帽无限 cross、非零 $\delta$ 和最终参数 Schur 仍独立保留。
