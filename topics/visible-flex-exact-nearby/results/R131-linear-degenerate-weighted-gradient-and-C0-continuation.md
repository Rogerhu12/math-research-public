# R131：准确线性退化结构、加权角梯度与仅需 C0 误差的真实延拓

2026-11-13，visible-exact-astra-ac0d。

**本篇结论。** R126 的两条真实 Riemann 方程存在准确的加权角梯度
线性输运系统。只要真实变量保持有界、$K<0$、$|p-q|$ 有严格下界，
角一阶导数就只能按一个显式线性系数增长。因此，验证真实分支的继续存在
只需候选的完整 $C^0$ 残差、候选一阶角导数、$C^0$ 误差屏障与非退化门；
不再需要通过 R126 的 $C^1$ 误差 Riccati 屏障。

独立 native consumer 已在 R129 同一数据上通过全部 168 个闭盒，覆盖
$0\le r\le1/200$、全实角及完整 $|\eta|\le10^{-9}$ 参数盒。它另从真实
腰相位计算初始加权梯度，再传播出实际一阶导数的有限有向上界。
这不是新的曲率目标，也没有改变初始腰、mean 或真实分支。

本篇不通过 $K=0$，不提供正帽或 regular 极点接合，也不宣告全闭面完成。

## 1. 系数、方向和固定对象

固定 R125–R130 的同一目标
$$
g_0=E(r)\,dr^2+a(r)^2d\theta^2,\qquad
K=-\frac{a''}{aE}+\frac{a'E'}{2aE^2}.
\tag{131.1}
$$
$E$ 是原始候选 $|F_r|^2$ 的完整角平均；任何后续等距分支都不重新定义它。
在一个实际公共 scalar germ 的严格负曲率区中，置
$$
k=\sqrt{-K},\quad \gamma=\frac{\sqrt E}{a}>0,\quad
\beta=\frac{a'}a,\quad
\kappa=\frac{k'}{2k}=\frac{K'}{4K}.
\tag{131.2}
$$
最后一个式子的分母是 $4K$，不是 $-4K$。
R126 的完整物理角变量满足
$$
\begin{aligned}
p_r&=\gamma q\,p_\theta+f(p,q),&
f(p,q)&=-\beta q(1+p^2)+\kappa(p-q),\\
q_r&=\gamma p\,q_\theta+g(p,q),&
g(p,q)&=-\beta p(1+q^2)-\kappa(p-q).
\end{aligned}
\tag{131.3}
$$
这里 $p=(B+k)/C$、$q=(B-k)/C$；两场曲率中的 $B$ 不等于相位函数。
实际特征导数取
$$
D_p=\partial_r-\gamma q\partial_\theta,\qquad
D_q=\partial_r-\gamma p\partial_\theta.
\tag{131.4}
$$
故第一条特征的角速度为 $-\gamma q$，第二条为 $-\gamma p$。
这也是该主部线性退化的具体含义：第一条速度与 $p$ 无关，第二条与 $q$
无关。以下证明直接运算方程，不以这个名称替代任何估计。

## 2. 两条准确加权梯度恒等式

定义
$$
d=p-q,\qquad U=d\,p_\theta,\qquad V=d\,q_\theta.
\tag{131.5}
$$
$d$ 可以为负，证明不把它误当成正 gap。直接相减给
$$
f-g=d\,[\beta(1-pq)+2\kappa].
\tag{131.6}
$$
令 $H=\beta(1-pq)+2\kappa$。由 (131.3)–(131.4) 得
$$
D_p d=dH-\gamma d\,q_\theta,\qquad
D_q d=dH-\gamma d\,p_\theta.
\tag{131.7}
$$
另一方面，$\gamma$ 没有角依赖，所以
$$
\begin{aligned}
D_p p_\theta
 &=\gamma q_\theta p_\theta+f_p p_\theta+f_q q_\theta,\\
D_q q_\theta
 &=\gamma p_\theta q_\theta+g_p p_\theta+g_q q_\theta.
\end{aligned}
\tag{131.8}
$$
把 (131.7) 与 (131.8) 代入乘法法则，所有
$\gamma d p_\theta q_\theta$ 项准确抵消。得到
$$
\boxed{\begin{aligned}
D_pU&=\big[\beta(1-3pq)+3\kappa\big]U
       -\big[\beta(1+p^2)+\kappa\big]V,\\
D_qV&=-\big[\beta(1+q^2)+\kappa\big]U
       +\big[\beta(1-3pq)+3\kappa\big]V.
\end{aligned}}
\tag{131.9}
$$
特别是，两个对角项中的 $3\kappa$ 同号。
第二条非对角项含 $q^2$，第一条含 $p^2$。
该恒等式保留完整零模和所有角频率。

脚本用独立 SymPy 多项式展开逐项核验 (131.6)、(131.9) 的两条式子，
以及第 7 节的两条带残差式子；五个多变量多项式都准确为零。
这不是抽取有限角点后检验等式。

## 3. 实际一阶导数的线性增长界

在一个闭径向区间上，假定
$\max_\theta(|p|,|q|)\le M(r)$，且有关系数可积。令
$$
W(r)=\max\big(\|U(r)\|_\infty,\|V(r)\|_\infty\big),\qquad
L(r)=|\beta|(2+4M^2)+4|\kappa|.
\tag{131.10}
$$
(131.9) 的每一行绝对值和不超过 $L$，因为
$$
\begin{aligned}
|\beta(1-3pq)+3\kappa|
 &\le |\beta|(1+3M^2)+3|\kappa|,\\
|\beta(1+p^2)+\kappa|,
|\beta(1+q^2)+\kappa|
 &\le |\beta|(1+M^2)+|\kappa|.
\end{aligned}
$$
沿两个各自的真实特征积分，再取完整周期角的 supremum，给
$$
D^+W\le LW,\qquad
W(r)\le W(r_0)\exp\!\left(\int_{r_0}^rL(t)\,dt\right).
\tag{131.11}
$$
只要 $\inf_\theta|p-q|\ge g_*(r)>0$，立即得到
$$
\max_\theta(|p_\theta|,|q_\theta|)
\le\frac{W(r_0)}{g_*(r)}
\exp\!\left(\int_{r_0}^rL(t)\,dt\right).
\tag{131.12}
$$
这控制的是实际解的一阶角导数，不是它与候选的导数误差。
即使这个界数值较大，只要它在有限验证区间上有限，仍排除有限时一阶爆破。
$\gamma$ 只改变特征路径，不出现在 (131.10) 的增长系数中；
不能据此把 $\gamma$ 从零阶误差比较中删除。

## 4. 仅需零阶误差的延拓定理

取连续、周期、分片径向光滑的明确候选 $P,Q$。
在所有分片端点匹配相同函数；若存在跳跃，必须单独支付该实际跳跃误差，
本篇 native 候选没有此类跳跃。候选可以由有限 $\widehat B,\widehat C$
和真实 $k$ 经 R126 (126.24a) 构造。

对全实角、完整参数盒及每个实际径向闭盒，给出有向界
$$
\begin{gathered}
\max(|P|,|Q|)\le\widehat M,\qquad
\max(|P_\theta|,|Q_\theta|)\le D_1,\\
\max(|R_P|,|R_Q|)\le\rho_0,\qquad
\inf_\theta|P-Q|\ge\widehat g>0,
\end{gathered}
\tag{131.13}
$$
其中 $R_P,R_Q$ 对应真实系数、完整未投影方程。
设一个预定管宽 $T_0>0$，并设连续非负屏障 $y$ 从严格大于真实初误差
$\epsilon_0$ 的值开始。在误差尚未退出管时，取
$$
M_b=\widehat M+T_0,\qquad
A_0=\gamma D_1+|\beta|(1+3M_b^2)+2|\kappa|.
\tag{131.14}
$$
假设全区间上严格通过
$$
y'\ge A_0y+\rho_0,\qquad
y<T_0,\qquad
\widehat g-2y>0,\qquad k>0.
\tag{131.15}
$$
所有下界在有限闭覆盖上保持统一严格正余量。
另假定 $a,E$ 的真实正下界、有限上界以及必要的分片光滑性；
本篇输入 provider 已逐盒核验这些目标条件。
初始真实腰数据光滑，$C_0$ 远离零，因此 $W(r_0)<\infty$。

**定理。** R125 从同一腰初值产生的真实局部分支延拓到整个验证区间，
满足
$$
e_0:=\max(\|p-P\|_\infty,\|q-Q\|_\infty)\le y.
\tag{131.16}
$$
并可在 (131.10) 取
$M=\widehat M+y$，在 (131.12) 取 $g_*=\widehat g-2y$。
这条结论不以候选二阶角导数、角残差导数或 $C^1$ 误差屏障为前提。

**证明。** 在真实局部分支存在时，沿 (131.4) 的实际特征，
$$
D_p(p-P)=\gamma(q-Q)P_\theta+f(p,q)-f(P,Q)-R_P.
$$
$f,g$ 的 Jacobian 行绝对和在 $|p|,|q|,|P|,|Q|\le M_b$ 上不超过
$|\beta|(1+3M_b^2)+2|\kappa|$。
故 R126 的准确零阶比较给 $D^+e_0\le A_0e_0+\rho_0$。
微分屏障和严格初值推出 (131.16)，严格管余量排除首次退出。

在此真实存在区间内，(131.9)–(131.12) 给统一有限的实际一阶导数。
因此真实速度 $-\gamma q,-\gamma p$ 在角变量中统一 Lipschitz，且真实
零阶值一直在非退化的有界区域内。反变换
$$
C=\frac{2k}{p-q},\qquad
B=k\frac{p+q}{p-q},\qquad A=Cpq
\tag{131.17}
$$
没有分母趋零；$|p-q|\le2M$ 与 $k>0$ 也给 $|C|\ge k/M>0$。

为明确接续所需的高阶正则性，对 (131.3) 作 $n\ge2$ 次角微分。
最高阶项仍是各自的 $\gamma q\partial_\theta$、
$\gamma p\partial_\theta$ 输运，另外的 $n$ 阶未知只线性出现：
例如 $\partial_\theta^n(qp_\theta)$ 除主部外的最高阶项为
$nq_\theta\partial_\theta^np+p_\theta\partial_\theta^nq$。
其系数由已控制的零、一阶导数给出，其余项只含更低阶角导数。
归纳应用线性特征积分界，任一固定有限阶角导数都在有限时间上有界。
由 PDE 本身又控制一侧径向导数。冻结速度与源的短时特征 Picard 构造
在 $C^0$ 中收缩，并由这些导数界给经典极限；存在时长可在该有界区域内
统一选取。因此一个有限最大存在端点不能落在 (131.15) 严格成立的区域内。
这排除了把估计误当成存在性假设的循环。

对实际有限个 scalar germs 逐片应用。目标 $a,E,K,k$ 和初迹在接点匹配；
$\kappa$ 可按一侧 germ 跳跃，但有界分片积分仍可用，$p,q,U,V$ 不跳跃。
由 (131.17) 得连续 $A,B,C$，再用 R126 的完整周期框架重建及
(126.27) 得真实 $C^2$ 浸入。腰偶对称按 R125 反射，二阶迹相同。
所有参数使用同一套有向界逐个应用，因此结论覆盖完整参数盒。
证毕。

该定理只替代原 $C^1$ 误差的存在门。若另一个用途确实需要很小的
导数误差，仍须另外验证它，不能把 (131.12) 的实际导数界称成误差界。

## 5. 真实初始加权梯度和闭盒消费者

腰上的精确有限相位给
$$
B_0=0,\qquad
C_0(\theta)=-\frac{1+\sum_j4j b_j(0)\cos(4j\theta)}{a(0)}.
\tag{131.18}
$$
这保留 mean $-1/a(0)$。由 $p_0=k_0/C_0$、$q_0=-k_0/C_0$ 得
$$
U_0=-\frac{2k_0^2C_{0,\theta}}{C_0^3},\qquad V_0=-U_0.
\tag{131.19}
$$
native 初值计算使用 provider 的 `exact_initial_C_polynomials(1)`，
先对真实区间 Fourier 系数求角导，再形成全角 16384 个闭格；
它没有从浮点轨迹求导，也没有删除相位系数的不确定性。
真实 $k_0^2=-K_0$ 则仍消费完整 primitive 和全部无限尾。

令一盒长度为 $h$、初屏障为 $s$，并用该盒完整上界构造 $A_0,\rho_0$。
脚本先检查 $1-hA_0>0$，再向外取
$$
t=\operatorname{up}\!\left[
\frac{s+h\rho_0}{\operatorname{down}(1-hA_0)}(1+2^{-40})+2^{-180}
\right].
\tag{131.20}
$$
它随后独立有向检验
$$
t>s,\qquad
\operatorname{down}\big[t-s-h(A_0t+\rho_0)\big]>0.
\tag{131.21}
$$
因此真正使用的是该盒上的仿射函数
$y(r)=s+(t-s)(r-r_l)/h$，不是把终点常数误称为微分屏障。
再检查 $t<T_0$、$\widehat g-2t>0$、$k>0$。
加权梯度则以该盒实际上界 $M=\widehat M+t$ 传播
$$
W_{\rm end}=\operatorname{up}\big[W_{\rm start}\exp(hL)\big].
\tag{131.22}
$$
前盒终值直接作为下盒初值。所有盒与实际公共 germ 的从属关系、闭覆盖
连续性和请求区间相等都以准确有理数检查。

消费者不读取输入中的 `D2`、`rho1` 或 `epsilon1`。
输入 producer 可以完全省去这些字段，只保留真实 $C^0$ 合同。
原报告里单一全局 $C^0/C^1$ 屏障失败也不妨碍本篇；不完整残差覆盖仍拒绝。

## 6. 已实际通过的完整数值实例

固定辅助参数
$$
\delta=-\frac{7789843107295549}{4611686018427387904}+\eta,
\qquad |\eta|\le10^{-9}.
$$
输入为 R129 的原始真实残差报告，完整区间 $[0,1/200]$，168 盒。
采用 256-bit Arb、$T_0=1/16$、512 个 primitive 节点及其原有完整尾，
不是只核参数中心。

| native 有向量 | 安全外舍入值 |
|---|---:|
| 初始 $C_0$ 范围 | $-7.593297107<C_0<-0.346523179$ |
| 初始 $|C_{0,\theta}|$ | $<175.977148478$ |
| 初始 $W_0$ | $<221.387250615$ |
| 零阶初屏障 | $<4.214339712\times10^{-10}$ |
| 完整区间末零阶误差 | $<0.026273878216$ |
| 实际 $|p-q|$ 全域下界 | $>0.192950665314$ |
| 真实 $k$ 全域下界 | $>0.924901682883$ |
| $\int L$ 的完整有向上界 | $<0.015631483553$ |
| 末端 $W$ | $<224.875050507$ |
| 实际 $\max(|p_\theta|,|q_\theta|)$ 全域 | $<1165.453616$ |

全部 168 盒的六项门均通过；报告保存各盒正微分余量、实际 gap、初末
误差屏障和加权梯度。最后一项是为存在性提供的粗有限界；R129 已有的
更小 $C^1$ 误差界仍保留，不用该粗界替换精确几何预算。
本篇证明同一个 R125 分支的延拓，因此 R129 已单独认证的嵌入结论仍指向
同一分支，没有产生另一条未经闭角检查的曲面。

native 命令（依赖路径按执行环境提供）：
```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python scripts/fourfold_codazzi_linear_degeneracy.py \
  --out notes/2026-11-13-R131-C0-only-r005-native.json.gz
```

核心绑定：

| 文件/输入 | SHA-256 |
|---|---|
| `scripts/fourfold_codazzi_linear_degeneracy.py` | `8b4e003df87bbfd685254dda1113d22b746b9be619d38628bd6d909195921933` |
| `notes/2026-11-13-R131-C0-only-r005-native.json.gz` | `be7f67eec3fd07a4057b7db351484d2c8360c93b3461f5b39fcebb6fff790f2e` |
| R129 原始完整残差报告 | `52c0a81f7e56db0be0a7c1001ab139200e4539870c77c5b5a75ff3b9e07ac536` |
| 原始残差 producer | `1c97e0bd58d49514501ede6d98b909567fb59d933813d2cc74d9e2813fc60258` |
| 真实目标/初值 provider | `6bc8f108e89bef96134c580be6ae18b382dae5b5ab6139e5863acdfa526f73bb` |
| 原始完整有限径向候选 | `a3e43fc8ee7ab8b6a0e080edccb107ac1e2d92634b0325783f7a99711cf6842f` |
| 同一精确仿射对象 | `91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848` |

全部仓库内传递依赖及 origin/direction 文件另列于同日 R131 manifest；
报告本身保留运行精度、依赖摘要和五项准确符号核验结果。

## 7. 可选的线性加权导数误差比较

本节不是第 6 节认证的必要门，但给确实需要导数误差时的准确替代式。
令
$$
\widehat d=P-Q,\quad
\widehat U=\widehat d P_\theta,\quad
\widehat V=\widehat d Q_\theta.
$$
把候选残差写回方程，乘法法则准确给候选的 (131.9)，附加源分别为
$$
S_U=(R_P-R_Q)P_\theta+\widehat d\,\partial_\theta R_P,
\qquad
S_V=(R_P-R_Q)Q_\theta+\widehat d\,\partial_\theta R_Q.
\tag{131.23}
$$
设
$$
e_W=\max(\|U-\widehat U\|_\infty,\|V-\widehat V\|_\infty),
\quad \widehat W_j\ge
\max(\|\partial_\theta^j\widehat U\|_\infty,
     \|\partial_\theta^j\widehat V\|_\infty).
$$
若实际和候选的 $|p|,|q|,|P|,|Q|$ 都不超过 $M$，则
$$
\boxed{
D^+e_W\le L e_W+
\big[\gamma\widehat W_1+8|\beta|M\widehat W_0\big]e_0
+\max(\|S_U\|_\infty,\|S_V\|_\infty).
}
\tag{131.24}
$$
证明中，沿实际第一特征，候选方程多出
$-\gamma(q-Q)\widehat U_\theta$。
两个矩阵系数差分别有界于 $6|\beta|M e_0$ 和 $2|\beta|M e_0$，
给 (131.24)；第二条相同。这里没有任何 $e_W^2$ 项。
若只持有普通残差界，可用
$$
\max(\|S_U\|_\infty,\|S_V\|_\infty)
\le2\rho_0D_1+2\widehat M\rho_1.
\tag{131.25}
$$
最后由
$d(p_\theta-P_\theta)=U-\widehat U-(d-\widehat d)P_\theta$
得到
$$
e_1\le\frac{e_W+2D_1e_0}{g_*}.
\tag{131.26}
$$
这是一条将来可消费的线性误差路线。它需要相应的有向输入，不能把本篇
只读取零阶残差的 native 运行说成已经验证了 (131.24) 的数值屏障。

## 8. 对后续验证的实际作用

新的连续残差 producer 为延拓用途只需保存真实 $\rho_0,D_1$ 及目标系数，
连同明确有限候选、初始零阶误差和逐盒非退化下界。初始 (131.19) 可复用
同一真实腰证书。消费者始终核对全部输入 SHA 和准确径向闭覆盖。
这降低所需角导数阶数，但没有放松全角、全参数、全 primitive 尾、真实
目标以及正 gap 的要求。

接下来要延长的仍是同一固定目标的真实分支；遇到 $K=0$ 或 $C=0$ 仍须
另换方程/图并支付正确匹配条件。R131 本身没有解决这些全闭面缺口。
