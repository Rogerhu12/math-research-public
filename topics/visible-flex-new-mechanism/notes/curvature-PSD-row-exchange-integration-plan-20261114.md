# 同度量曲率上界与稀疏约束交换的后续接口

日期：2026-11-14。状态：**纸面实现计划；没有实现或运行新的曲率求解**。本稿不改已经部署的 metric exchange 源码、目标或预算。是否采用，先取决于当前公开运行的新状态及完整实际审计。

直接依据为 [R103](../results/R103-actual-metric-curvature-semidefinite-gates.md) 和已发布的 `scripts/frame_curvature_psd.py`。R103 已给实际诱导度量下的准确四 PSD 行及完整参数导数；本稿仅明确如何接入现有全网值检查/稀疏 Jacobian 框架，避免把尚不可行的固定曲率门当成可行初态。

## 1. 两种任务必须区分

最终设计目标仍为
$$
 \tau_* = \frac{61}{1000},\qquad
 \max_i|\kappa_i|\le\tau_*^{-1}=\frac{1000}{61}.
$$
它比核心直径下界 $D\ge2$ 单独给出的必要值 $50/3$ 略强，且只是当前选择的 reach 设计值。通过该局部曲率门仍不能认证全曲面 reach。

如果下一 metric exchange 合格态的曲率仍显著高于 $1000/61$，直接把这一固定目标作为硬行会使新求解没有已知可行初态。这里建议的后续阶段是：

1. 冻结同一个完整 $g$、$b_0$、物理族和参数盒。
2. 用明确的固定 $\bar\eta<1$ 保持已达到的实际度量水平。$\bar\eta$ 必须根据已保存的新态及所选完整网格显式确定；不能偷偷沿用失败的旧辅助 $\delta$。
3. 引入一个正的**非物理**辅助主曲率上界 $\lambda$，最小化 $\lambda$，其初值由当前全网直接主曲率最大值加明确裕量确定。
4. 最终独立报告是否已经达到 $\lambda_* =1000/61$ 的设计门；没有达到时只记录曲率上界阶段进展。

这是带固定 metric 预算的曲率极小极大任务，不是追加旧 $L^2$ 目标，也不是把 $\lambda$ 放进物理曲面身份。若新态已通过目标曲率门，则更简单：保持固定 $\tau_*$ 的 R103 四行，继续减小度量误差即可。

## 2. 真实第一形式和曲率上界 epigraph

沿用 R103 的量：
$$
 A=X_s,\quad T=X_\theta/a,\quad
 U=X_{ss},\quad V=X_{s\theta}/a,\quad Z=X_{\theta\theta}/a^2,
$$
$$
 w=A\times T,\quad q=|w|>0,\qquad
 I=\begin{pmatrix}E&F\\F&G\end{pmatrix}
 =\begin{pmatrix}A\cdot A&A\cdot T\\A\cdot T&T\cdot T\end{pmatrix},
$$
$$
 K=\begin{pmatrix}e&f\\f&k\end{pmatrix}
 =\begin{pmatrix}w\cdot U&w\cdot V\\w\cdot V&w\cdot Z\end{pmatrix},
 \qquad II=K/q.
$$
即使当前真实 $|T|$ 在浮点评价中几乎等于 $1$，曲率接口也继续用这个实际 $G=T\cdot T$，不直接代入目标单位矩阵。

对 $\lambda>0$，准确等价式为
$$
 \max_i|\kappa_i|\le\lambda
 \quad\Longleftrightarrow\quad
 H_\pm(\lambda):=\lambda qI\pm K\succeq0.
 \tag{1}
$$
证明是 R103 的 $qI\pm\tau K\succeq0$ 在 $\tau=1/\lambda$ 时乘以正数 $\lambda$。所以四行可取
$$
 r_\pm=\operatorname{tr}H_\pm,\qquad
 d_\pm=\det H_\pm.
 \tag{2}
$$
不可只留行列式：两个负特征值的乘积也是正的。也不可删除 $q>0$ 的正则性前提；退化 $q=0$ 会使原平方/PSD表达式误给零值。

为了避免 $\lambda$ 约为几十时迹与行列式的量级过大，可以预先固定正尺度 $\lambda_{\rm ref}$，例如准确常数 $100$，改用 $\zeta=\lambda/\lambda_{\rm ref}$ 和
$$
 \widehat H_\pm=\zeta qI\pm K/\lambda_{\rm ref}.
 \tag{3}
$$
它只对矩阵乘了固定正数，不改变可行集合。这个数值缩放须进入新 objective identity；不得随试探态或当前最坏曲率悄悄变化。后面给无缩放 $\lambda$ 的公式，缩放版只需按 (3) 替换。

## 3. 完整参数与辅助列导数

当前 $a$ 是已冻结的完整函数，所有物理参数方向 $\partial_p a=0$。R103 已给
$$
 \partial_pH_\pm
 =\lambda\big[(\partial_pq)I+q\,\partial_pI\big]
 \pm\partial_pK.
 \tag{4}
$$
其中 $\partial_pK$ **必须**包含 $\partial_pw$ 与三个二阶位置 jet 的变化，不能只求固定法向下的二阶导数。

对辅助量本身，物理曲面完全不变：
$$
 \partial_\lambda H_\pm=qI.
 \tag{5}
$$
若 $h_{11},h_{12},h_{22}$ 是 $H_\pm$ 的分量，则
$$
 \partial_\lambda r_\pm=q(E+G),
$$
$$
 \partial_\lambda d_\pm
 =q\big(Gh_{11}+Eh_{22}-2Fh_{12}\big).
 \tag{6}
$$
任一物理列则为
$$
 \partial_pr_\pm=\partial_ph_{11}+\partial_ph_{22},
$$
$$
 \partial_pd_\pm
 =h_{22}\partial_ph_{11}+h_{11}\partial_ph_{22}
 -2h_{12}\partial_ph_{12}.
 \tag{7}
$$
对缩放变量 $\zeta$，$\partial_\zeta\widehat H_\pm=qI$，式 (6) 对 $\widehat H$ 原样成立。物理列中的第二形式换成 $K/\lambda_{\rm ref}$。

可以复用现有固定 $\tau$ helper，而不在 helper 内暗改其约定：在当前辅助量取 $\tau=1/\lambda$，迹行及其物理 Jacobian 乘 $\lambda$，行列式行及其物理 Jacobian 乘 $\lambda^2$；再按 (6) 独立填辅助列。调用者必须明确其当前 $\lambda$ 和同一物理态，不能把一次 helper 缓存用于另一个辅助值。

只改变 $\lambda$ 时，$I,K,q$、全部物理 jet 和它们的 Jacobian 都可复用；只重新形成四行及辅助列。改变物理系数才重新计算曲面。

本阶段最后一列的含义必须明确改为曲率上界。固定 metric 预算行对这列的导数是零，不能复用旧 metric epigraph 的 $1+f_m^2/\delta^2$ 辅助列。球、条带、镜像、帽高等行对它也都是零。旧 metric 辅助值只作为输入历史保留；$163$ 维物理态身份不含旧 $\delta$ 或新 $\lambda$。

## 4. 固定 metric 预算和所有旧门继续全网检查

可用与目前 epigraph 完全相同的两个光滑行给固定 $\bar\eta$：
$$
 \bar\eta-e_m-\frac{f_m^2}{\bar\eta}\ge0,
 \qquad
 \bar\eta+e_m-\frac{f_m^2}{\bar\eta}\ge0,
$$
其中 $e_m=|X_s|^2-1$、$f_m=X_s\cdot T$。$\bar\eta$ 在本阶段固定，不是另一个优化变量；还须独立直接核真实最大 $\eta\le\bar\eta$。

保留同一帽高行、物理参数盒、正高度、球 $101/100$、当前内条带 $38999/100000$ 和镜像目标 $61/1000$。不能为了改善曲率而恢复旧的条带超量或降低帽高。曲率不替代镜像门，镜像门也不替代曲率门。

每个新物理态完整重建全网普通两阶 jet，然后一次得到：

- 所有原来的七组值，其中两条 metric 行现在使用固定预算；
- 当前 $\lambda$ 的四 PSD 行；
- 独立直接主曲率最大值、峰位、各区域值；
- 独立正则性、真实 metric 和全部包络/镜像门。

值网格检查不能仅遍历 Jacobian 池。选点至少分两类：

1. 在原几何门及固定 metric 预算下，实际最大曲率最低的物理态。
2. 另外满足当前辅助 $\lambda$ 四行和直接 $\max|\kappa_i|\le\lambda$ 的辅助可行态。

前者可以改善但仍没有达到最终 $\tau_*$ 目标，必须另报目标通过布尔值及缺口。最终 $\tau_*$ 四行必须用同一物理态独立重算；不能用保存的较大 $\lambda$ 自动代替它。

## 5. 同一稀疏交换算法中的增加方式

现有值网格有七组行，增加四组即十一组。初始可在每径向行给每条 PSD 行取最危险的一个角，加入旧池；如果采用当前旧池初始化的上界 $1440$ 行，则新增最多 $640$ 行，总计 $2080$ 行。

每轮固定整个池；回调/轮末在完整十一组值上分离遗漏违反，按既定策略增广，不删除旧行。每次主迭代和每个候选的曲率正则性与直接最大主曲率仍独立核验。池外 PSD 违反的点不能因为它的 $\eta$ 小就被标成满足当前 $\lambda$。

共享的物理评价/时间/轮数预算、每轮进入和退出原因、完整新行索引，都沿当前交换框架保存。不同组的迹与行列式量纲不同，采用固定缩放时也要分别给出明确的数值容差与独立曲率判定；不能只靠一个很松的原始 determinant 容差来接收曲率点。

如果任一试探态不满足 $q>q_{\min}$，R103 helper 应继续明确拒绝。不得用把 $q$ 替为 $\sqrt{q^2+\epsilon^2}$ 的做法伪称准确 R103 行。初态正则不保证所有 SLSQP 试探点正则；最小实现可以在越界时保留此前合格态并明确失败退出，或另建有记录的域保护策略，但不能把这个技术问题隐藏在曲率值中。

## 6. 二阶参数导数的真实接口

完整带 entry/Q 的物理类已经提供

```python
problem.geometry(state, radial, theta, order,
                 jacobian=True, full_two_jet_jacobian=True)
```

后续调用必须消费 `jac_Xs`、`jac_Xt`、`jac_Xss`、`jac_Xst`、`jac_Xtt` 五项。R103 接口要求的缩放是
$$
 \partial_pT=\partial_pX_\theta/a,\quad
 \partial_pV=\partial_pX_{s\theta}/a,\quad
 \partial_pZ=\partial_pX_{\theta\theta}/a^2.
$$
必须保留新增 Q 列和实际 entry 权重的二阶径向导数，不能只从旧一阶缓存推断。当前独立高度列的 $X_{ss}$ 导数含高度基 $C_j'$，而 $X_{s\theta}$、$X_{\theta\theta}$ 的高度列为零；这与共同中心函数的准确构造相符，不能误用旧辅助 beta 列。

## 7. 分批求导为何不改变曲面

现有物理定义为
$$
 X(s,\theta)=a(s)\Pi T(s,\theta)+z_c(s)e_z.
$$
$\Pi$ 是每个固定 $s$ 的整圈固定规范原函数，$z_c$ 已使用与查询节点无关的固定物理分区原函数。因而某个径向行的值和其参数导数不依赖同一次调用还列了哪些其他径向行。**这一事实依赖当前查询无关的中心 evaluator**；不能用于旧四稀疏节点逐段积分出另一帽高的实现。

可以把需要 Jacobian 的径向索引分批，每批最多 $16$ 个真实行，额外加入 $s=0,L$ 以满足完整 chart 调用前提。每批保持同一个完整 $384$ 角网、同一共同原函数规则、GH 规则、固定 $a$ 和全部物理系数。调用完整二阶 Jacobian 后，仅抽该批中当前池需要的点和行，随后释放其大数组。

这里没有拼接新曲面、没有新增几何端口或各批独立平移。$0,L$ 只是既有物理曲面的重复查询端点，不可重定中心高度。批结果与完整无 Jacobian 网格的普通 $X$、全部二阶 jet 及共同中心逐点比较，差值只记录为浮点评价一致性；不能把有限误差比较升级为连续证书。

人工检查需要先覆盖同一小模型的全批/分批五项 Jacobian和普通六jet，再用原 R103 人工图 jet 检查各组链式。研究态批处理只在新的公开 Actions 阶段运行。当前 frozen metric exchange 不加入这一调用。

## 8. 内存账

对 $N_r=160,N_\theta=384,n=163$，一个三向量参数 Jacobian 占
$$160\cdot384\cdot3\cdot163\cdot8=240353280\text{ bytes}.$$
现有完整接口返回七个这类数组时，光返回值就约 $1682472960$ 字节，尚未计入构造过程的参数 tangent jets、FFT 暂存、基底缓存和普通两阶 jet。不能因为只保四条曲率行，就先无条件构造并常驻整网七张大数组。

对 $16$ 个实际行加两个端点的最坏 $18$ 行批次，一个三向量 Jacobian 为 $27039744$ 字节，七张为 $189278208$ 字节。该数也不是进程峰值上界，实际构造仍有临时数组；它至少把单次返回值的尺度降了近九倍。

十一组全网 $164$ 列矩阵需要 $886702080$ 字节，仍不得构造。初始 $2080$ 行池只需 $2728960$ 字节；完整十一组普通值约 $5406720$ 字节，保留它们以持续全网筛查是合理的。全网普通基底与各批求导基底可能同时缓存，需单列真实 RSS、最大批数组、选行导数缓存字节和准备耗时，不把分批标签当成已证内存界。

## 9. 仍未支付的事情

本方案没有证明当前物理族存在同时近等距、厚度足够的状态；没有证明新曲率阶段一定改善；没有接全时连续等距族或完整远场法弦证书。它的用途是：一旦当前 exchange 得到带内条带裕量的可信新初态，下一阶段可以真实控制局部曲率而不偷换实际度量、不丢二阶参数项、不丢全网门，并能以可追溯方式区分曲率辅助上界、最终 $\tau_*$ 目标和仍缺的全 reach 证明。
