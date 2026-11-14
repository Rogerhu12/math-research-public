# 实际完整帽 mismatch 的角导数入口与 01:02 原生重放

2026-11-13，reproduce-newton。正文给新入口的数学合同和已实际运行范围。
完整强通量定理使用
notes/2026-11-12-core-strong-weak-residual-contract.md §7；
本篇不重命名弱 PDE residual，也不把旧 $R_0$ gap 当成新的 $R_1$。

## 1. 对象、范数和尚欠的整体输入

对象仍是准确显式对称族
$\delta_5=-7789843107295549/4611686018427387904$，
实参数半宽 $\eta=10^{-9}$，物理接口 $c=1/4$。
完整帽包括 $[1/4,3]$ body、$[3,25/8]$ 自然接合和同一真 Robin 尾。
角采用 Fourier 平均内积，频率为 $4k$；regular 输入 $\xi$ 及其通量
$\lambda$ 都保留。保存的有限试函数有十个输入列，内部物理模式
$|k|\le16$，径向为 P2；这不是对实际方程作相同的体投影。

对同一准确试函数 $V$ 和全域散度零通量 $j=(P,Q)$，
新两个 Gram 正是
$$
 G_0[g]=\int (B\nabla V_g-j_g)^*B^{-1}(B\nabla V_g-j_g)
       +\sum_{k\ne0}\frac{|\,\Gamma_k V_{g,R,k}+P_{g,R,k}\,|^2}{\Gamma_k},
$$
$$
 G_1[g]=\int D(B\nabla V_g-j_g)^*B^{-1}D(B\nabla V_g-j_g)
       +\sum_{k\ne0}\frac{(4k)^2
          |\,\Gamma_k V_{g,R,k}+P_{g,R,k}\,|^2}{\Gamma_k},
 \qquad D=\partial_\theta.
$$
$R_j=\sqrt{G_j[g]}$。导数在加权之前作用；它不是
$D(B^{-1/2}(B\nabla V-j))$。有限输入间的全部交叉项都保存。

两个入口分别是：

- scripts/fourfold_phase_cap_angular_mismatch.py：实际 body 闭径向区间；
- scripts/fourfold_phase_cap_graft_angular_mismatch.py：完整自然接合及真 Robin 项。

任意一份部分报告都明确写 full_cap_complete=false。一个完整帽的
$R_0,R_1,C_B$ 必须收集整个 $[1/4,25/8]$，不得把缺段补零。
整族 lift 还须使用 R111 的完整 form 比较或另付同族 lift。

## 2. 真无限 primitive 的角 AD

令 $P=\mathcal P(T)-e_r$ 为旋转柱坐标中的单位原函数差，
$P_r$ 是其真实径向导数。$P$ 和 $P_r$ 已含原函数的完整无穷尾。
由 $D e_r=e_\theta$、$D e_\theta=-e_r$，
$$
 DP=(T_r^{\rm cyl}+P_\theta^{\rm cyl},
     T_\theta^{\rm cyl}-1-P_r^{\rm cyl},T_z),
$$
其中本式右边的下标表示柱坐标分量，不能与径向导数混淆。
用无歧义的分量 $P=(P_0,P_1,P_2)$ 重写就是
$$
 DP=(T_0+P_1,T_1-1-P_0,T_2),\qquad
 DP_r=(T_{r,0}+P_{r,1},T_{r,1}-P_{r,0},T_{r,2}).
$$
实际单位切向量为
$$
 T=(-\cos\gamma\sin\beta,\ \cos\gamma\cos\beta,\ \sin\gamma).
$$
这些等式给真正无限原函数的角导数。程序不会把有限 FFT 原函数
的角导数当成精确 $T$。

新 ThetaJet 同时携带真实值和物理 $D$ 导数，对已有消去径向尺度
后的 form 公式作乘法、求逆和 sin/cos 的准确一阶 AD。
实际有限 $\beta,\gamma$ 的角频率为 $4k$；$\beta_r,\gamma_r$ 的
角导数及 $\beta_{\theta\theta},\gamma_{\theta\theta}$ 全部直接计算。
径向标量 $a,Z,K_0$ 的角导数准确为零。由此同时得到
$B_{11},B_{12},B_{22}$ 和 $DB_{11},DB_{12},DB_{22}$，
而只需原来那一次完整 primitive 计算。

整实参数盒在完整物理 scalar germ 形成以后统一加入。
ParameterDiskBody 已有准确中心 $\delta_5$，这里只加入
$[-\eta,\eta]$ 乘真实方向，不再加一次中心。不将参数拆进原始
样条控制点，也不抹掉复径向域上的虚部。

## 3. 完整角 gap、alias 和径向积分

在每个真实共同样条 span 内，对有限 P2 试函数逐 Fourier 系数构造
$$
 z_0=B_{11}R+B_{12}T-P,\qquad
 z_1=B_{12}R+B_{22}T-Q,
$$
$$
 Dz_0=(DB_{11})R+(DB_{12})T+B_{11}DR+B_{12}DT-DP,
$$
$$
 Dz_1=(DB_{12})R+(DB_{22})T+B_{12}DR+B_{22}DT-DQ.
$$
这里 $R=V_r,T=DV$。native Gauss 节点上保留全部十个输入列及
全部原有限输出模。最终有限矩阵中心是所选 binary64 Hermitian
矩阵，选择误差计入实际有向算术误差。

径向解析延拓只属于该真实 span 的 germ。外复盘上的完整
quadratic integrand 模数为 $M$，半区间长 $h$，外半径 $\rho>h$，
$n$ 点准确 Gauss 的费用取
$$
 \frac{4hM(h/\rho)^{2n}}{1-h/\rho}.
$$
它是解析延拓的界，未宣称在相邻真实 span 外仍是实际几何。
复径向 quadratic integrand 以系数共轭后的解析多项式定义，
不将复变量本身取共轭而破坏全纯性。

完整实径向区间上，归一角 $x=4\theta$ 的复带 $|\Im x|\le S$
给整个 integrand 模数 $M_\theta$，$N$ 点角梯形的完整费用为
$$
 \frac{2M_\theta e^{-NS}}{1-e^{-NS}}.
$$
真实原函数尾、实际节点球半径、Gauss 余项、完整角 alias 以及
Hermitian 中心选择费分别记录。这个别名费用作用于整个积分对象，
不是只对 $B$ 的某个低 Fourier 块。

实际首试 $N=1024,S=1/32$ 的 $R_1$ integrand 模数约 $1.72\times10^9$。
它使角 alias 密度超过目标；继续缩小径向格并不能解决此项。
已保留该 partial，并明确用 Ctrl-C 停止，退出码 130。
同一真实局部盒 $[1/4,262145/1048576]$ 的 $N=2048$ 检查实际给
$R_1$ alias 密度 $<5.532\times10^{-19}$。因此新默认值取 2048。
尚未在这个网格完成整个 body 积分。

## 4. $C_B$ 的直接实域公式

把真实 form 写成
$$
 B=\begin{pmatrix} A&A v\\Av&A v^2+\kappa\end{pmatrix},
 \qquad A,\kappa>0.
$$
在能量正交坐标
$(\sqrt A(u_r+v u_\theta),\sqrt\kappa\,u_\theta)$ 中，
$B^{-1/2}(DB)B^{-1/2}$ 与下面真实对称矩阵正交相似：
$$
 \begin{pmatrix}
  DA/A & \sqrt{A/\kappa}\,Dv\\
  \sqrt{A/\kappa}\,Dv&D\kappa/\kappa
 \end{pmatrix}.
$$
所以完整实域区间算术直接支付其两特征值模，不对 $B^{-1/2}$ 作
另一次数值求导。$S=0$ 的角覆盖仍包含全部角节点间隙。

01:02 恢复期间实际局部盒给
$C_B<44.530275$、$A>.04340022$、$\kappa>.00567897$。
这些是同一盒的连续全角/全参数结论，不是整个帽的最大值。

当前 flint 0.9 对横跨零的 arb 区间作一般幂 **2 可返回 nan。
新 graft 中 $(Dv)^2$ 已改为显式双线性乘积；ThetaJet 的整数幂本来
就用乘法实现。非负模数上界的平方和正底数幂不受该问题影响。
这一修正没有通过“丢掉 nan”放宽任何门。

## 5. 自然接合中的完整 8×8 kernel

在真实自然接合上，由已有无限 Wiener 范数给 $P,P_r$ 的完整角界，
再用上述准确 AD 得到 $B,DB,B^{-1}$。没有角网格，也没有遗漏
无穷 Fourier 模。

令
$$
 X=(R,T,P,Q,DR,DT,DP,DQ).
$$
$z=C_0X,Dz=C_1X$，其中
$$
 C_0=\begin{pmatrix}B_{11}&B_{12}&-1&0&0&0&0&0\\
 B_{12}&B_{22}&0&-1&0&0&0&0\end{pmatrix},
$$
$$
 C_1=\begin{pmatrix}
 DB_{11}&DB_{12}&0&0&B_{11}&B_{12}&-1&0\\
 DB_{12}&DB_{22}&0&0&B_{12}&B_{22}&0&-1
 \end{pmatrix}.
$$
实际 kernel 为 $K_j=C_j^*B^{-1}C_j$。选取准确对称 dyadic
$\widehat K_j$，全部条目区间给
$\|K_j-\widehat K_j\|\le\rho_j$。于是
$$
 \left\|\int X^*K_jX-\int X^*\widehat K_jX\right\|
 \le\rho_j\int\sum_{\ell\ {\rm active}}\|X_\ell\|_{\rm HS}^2.
$$
右边保留所有输入列，不能用某个采样列代替。
常 kernel 的积分用完整 Parseval 和准确三点 Gauss；
所有分量径向次数至多二，所以乘积次数至多四，Gauss 对该有限
多项式准确。球算术、所选中心和 kernel 区间变化分别收费。

这条新 graft 入口已完成 AST 和 imports，完整接合积分尚未运行。
其尾端子入口已经真实运行并 exit0。

## 6. 真 Robin 与 regular

$\Gamma_k$ 使用 finite_tail_entries 已证的真实外尾区间，覆盖同
$\delta_5\pm\eta$。每个非零物理模的两项是
$$
 |\Gamma_k V_{R,k}+P_{R,k}|^2/\Gamma_k,\qquad
 (4k)^2|\Gamma_k V_{R,k}+P_{R,k}|^2/\Gamma_k .
$$
$\Gamma$ 与 $D$ 准确交换。$\Gamma^{-1}$ 仅作用于非均值槽；
regular 输入列仍参与上述全部 Gram，regular 输出误差仍由
$C_{\rm lift,reg}R_0$ 独立支付。没有引入虚假的 $\Gamma_0$。

完整 body/graft/Robin 收齐后，§7 的投影界才给
$C_{\rm lift,N}(R_1+C_B R_0)$。若 R111 完整帽 form 比较给
$\varepsilon_{\rm cap}\le1/500$，则 R95 原短窗竞争函数在新族的
能量至多乘 $1+\varepsilon_{\rm cap}$，相应 lift 至多乘其平方根。
这些竞争函数的非均值真尾迹为零，所以不需要比较两个不同
$\Gamma$ 选择。该转授须读取完整 R111 证书；只有已观察的阈值
不构成新全帽 strong-flux 数值报告。

## 7. 实际重放状态与精确命令

实际已完成的范围和 stdout 数值另存
notes/2026-11-13-native-core-0102-observed-receipt.json。
它清楚区分完整文件尚未远存与已执行事实，不重建丢失矩阵。

已重新得到当前 paid-low NPZ 的原 SHA
aad06ad36773210c398c41b7f4b515631301d3e54f84322332d0fb49b6087837；
随后 6+7+4+4 逆及 whole-eta 40 行 strongGram 都完成，后者 NPZ
与前次 a35c292d... 准确一致。9 场真实 leaf60 矩形及其实连续
R110 gate 也已完成；它们只覆盖该小 leaf。其 H1/2 交换子上界
4508.913 很粗，不能由此声称整个核心传播常数可用。

恢复后在本题目录使用单线程环境：
~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_low_feedback_paid_inputs.py --bits 256 \
  --out notes/native_core_replayed/recreated_paid_low.json

python scripts/fourfold_phase_low_block_dihedral.py \
  --paid-low notes/native_core_replayed/recreated_paid_low.json \
  --height-order 0 --bits 256 \
  --out notes/native_core_replayed/finite_low_dihedral.json

python scripts/fourfold_phase_core_energy_fields.py \
  --leaf-report data/core_uniform_flow_ci/43307149760/block_60_80/span_0060_root.json \
  --out notes/native_core_replayed/energy9_leaf0060.json
python scripts/fourfold_phase_strict_core_energy.py \
  --field-report notes/native_core_replayed/energy9_leaf0060.json \
  --out notes/native_core_replayed/energy9_leaf0060_continuous.json

python scripts/fourfold_phase_cap_graft_angular_mismatch.py --tail-only \
  --out notes/native_core_replayed/true_tail_angular_mismatch.json
python scripts/fourfold_phase_cap_angular_mismatch.py --element 0 \
  --first-common-span 0 --last-common-span 1 --angles 2048 \
  --out notes/native_core_replayed/body_theta_element0_span0_N2048.json
python scripts/fourfold_phase_cap_graft_angular_mismatch.py \
  --out notes/native_core_replayed/graft_and_true_tail_angular_mismatch.json
~~~
普通 git promisor 首 manifest 在这次原生窗口已成功下载；
随后整个 175 目录的 sparse-add 在环境失联前未返回。
没有把未下载 binary 通过 connector 传送，也没有重算那 175 个原叶。
新环境再次可用时优先正常 materialize 原输入，再完成 global collector
和第六块装配；不要用这份 receipt 替代那两个完整报告。

整个课题仍欠完整强反馈及非线性闭合，本篇没有声称完成。
