# 当前真实根势的复条带、Fourier 尾与含均值根剪切费用

2026-11-12，independent-audit。完整证明与实际有向计算。

## 1. 对象、完成范围和真实数值

对象严格为 R83/R87 同一准确仿射族
\[
 \delta_5=-7789843107295549/4611686018427387904,\qquad
 |\delta-\delta_5|\le1/2500000.
\]
每个参数使用其真正移动根，半径区间、原始输入、仿射方向和 root
证书的 SHA 全部保留。源
scripts/fourfold_phase_root_potential_complex_strip.py 完成物理角域
\[
              |\operatorname{Im}\theta|\le1/256.
\]
它计算前半 quarter 的 128 个准确实角区间与上半条带的 16 个准确
虚角区间，共 **2048 个连续复矩形**；全部通过，无失败或遗漏格。
实共轭、真正 D4 反射和四重周期性补齐整个复条带与另一径向根。
这不是复点采样。

完成报告
notes/2026-11-12-actual-root-v0-complex-strip.json.gz 给
\[
 \begin{gathered}
 \operatorname{Re}Y_0'(\theta)>.0559300355832527,\\
 |v_0(\theta)|<6004.148324,\\
 8.32788647674253<q<11.67215062130776.
 \end{gathered}
 \tag{1.1}
\]
最后的 \(q=2\pi/\ell\) 来自 R83 完整圆长证书；程序核对它与复角
输入属于同一对象、同一 root 证书和同一准确参数盒。所有系数始终
以旋转柱坐标基表示，复旋转矩阵不被误当作 \(L^2\) 酉；几何双线性
点积和叉积则按其准确复正交恒等式处理。

## 2. 复相位的准确中心 Taylor 与无限位置原函数

每个相位仍是实际有限三角函数及准确径向 polynomial germ。
对它的第 \(i\) 个径向系数和第 \(j\) 个归一化角导数，在矩形中心
\(z_c\) 先求和。将真实函数展开到 \((z-z_c)^8\)，每个 mode 的
完整遗漏量为 R87(87.27)
\[
 |b_{im}|e^{4m(|\operatorname{Im}z_c|+h_{\rm im})}
           \frac{(4m)^{j+9}
           (h_{\rm re}^2+h_{\rm im}^2)^{9/2}}{j!\,9!}.
 \tag{2.1}
\]
每个实际 \(b_{im}\) 仍是包含整个参数族及真正根的球。所有 mode
费用相加，不把中点函数当作盒上真实函数。该中心展开保持不同
Fourier mode 之间的实际相消，从而避免旧独立矩形包络的过度膨胀。

位置的无限原函数先在 \(z_c\) 由 Q512 的真实 Fourier 系数和 R52
完整 alias/tail 求出。复条带宽度在输入 Fourier 预算中准确乘 4；
径向 jet 的尾按实际外盘 Cauchy 费逐项加入。然后使用真正旋转基
恒等式
\[
                     F_\theta=aT-J_{\rm rot}F.
 \tag{2.2}
\]
令 \(Z(z)=F(z)-F(z_c)\)，则
\[
 Z'=G-J_{\rm rot}Z,\quad Z(z_c)=0,\qquad
 G=aT-J_{\rm rot}F(z_c).
 \tag{2.3}
\]
对角矩形内任一线段，置
\(d=(h_{\rm re}^2+h_{\rm im}^2)^{1/2}\)。
由 \(|\cos w|\le e^{h_{\rm im}}\)、
\(|\sin w|\le |w|e^{h_{\rm im}}\)，水平两分量的变化模数分别不超过
\[
 e^{h_{\rm im}}\left(dM_1+\tfrac12d^2M_2\right),\qquad
 e^{h_{\rm im}}\left(dM_2+\tfrac12d^2M_1\right),
 \tag{2.4}
\]
竖分量不超过 \(dM_3\)，其中 \(M_j\) 为矩形上真正 \(G_j\) 的
模数界。该式逐径向系数使用；所有更高角系数再由 (2.2) 的准确
递推产生。这里没有对截断原函数免费作角微分。

## 3. 实际几何分母与势的解析性

沿用 R83 的真实旋转基变量
\[
 \begin{gathered}
 h=-\sin\beta X_1+\cos\beta X_2,\quad
 v=-\cos\beta X_1-\sin\beta X_2,\\
 Q=\cos\gamma X_3-\sin\gamma h,\quad W=Q^2+v^2,\\
 D=(1+\beta_\theta)\cos\gamma\,Q-\gamma_\theta v,\quad
 H=(T\times X)\cdot F,\quad \kappa=K_0/(r-t).
 \end{gathered}
 \tag{3.1}
\]
每一个实际复矩形都检查
\(\operatorname{Re}\kappa,\operatorname{Re}F_z,
\operatorname{Re}W,\operatorname{Re}D,\operatorname{Re}H>0\)。
因而对数、平方根和倒数全部有与实轴相容的唯一分支。
\(\kappa\) 先由真无限 \(E\) 的 root jet 形成；准确 \(K_0(t)=0\)
只去掉常数项，未对含零的曲率区间作除法。

实际
\[
 Y_0'=\frac{D}{\sqrt\kappa W},\qquad
 U=\frac{\kappa F_z^4W^2}{H^4},\qquad
 V_*=\frac{\kappa W^2}{D^2}
 \tag{3.2}
\]
及 R83 根势公式直接以复数球计算。源始终保留复值，未使用实轴
程序中的 real-jet 投影。以
\(\mathcal D=-\partial_r+(M/D)\partial_\theta\) 计算到二阶的
R83 公式给 \(v_0=-L_2-L_1^2/4\)。报告同时检查真正
\(\operatorname{Re}Y_0'>0\)，不是从单独分母不为零推断它。
因此 (1.1) 是完整复条带上的真实解析函数界。

## 4. canonical 逆条带与全 Fourier 尾

取实轴规范 \(Y_0(0)=0\)，令
\[
                  H_0(z)=qY_0(z).
 \tag{4.1}
\]
它是实际 analytic lift，满足
\(H_0(z+2\pi)=H_0(z)+2\pi\) 和
\(H_0(z+\pi/2)=H_0(z)+\pi/2\)。
若 \(\operatorname{Re}H_0'\ge qm>0\)，对条带内任意两点，
\[
 \operatorname{Re}\frac{H_0(z)-H_0(w)}{z-w}
       =\operatorname{Re}\int_0^1H_0'(w+t(z-w))\,dt>0.
 \tag{4.2}
\]
条带凸，所以 \(H_0\) 单射，且导数不为零。
又因 \(H_0\) 在实轴为实值，
\[
 \operatorname{Im}H_0(x+is)
       =\int_0^s\operatorname{Re}H_0'(x+it)\,dt.
 \tag{4.3}
\]
两条边界的虚部因此分别大于 \(qms\) 和小于 \(-qms\)。
局部逆沿任一较窄水平条带中的路径延拓时不能从竖向边界逃出；
周期 lift 的有界周期差也排除实方向有限值逃逸。故像包含每个
严格较窄的水平条带。安全取
\[
 s_\psi=\tfrac12q_-m/256
                >.0009097245839404.
 \tag{4.4}
\]

令 \(\widetilde v_0(\psi)=v_0(H_0^{-1}(\psi))\)。它在
\(|\operatorname{Im}\psi|\le s_\psi\) 解析，模数仍满足 (1.1)，
且只有 \(4\mathbb Z\) Fourier 模。准确移线积分给
\[
 \boxed{\quad
 |\widehat{\widetilde v_0}(4k)|
 \le 6004.148324\,e^{-4s_\psi|k|}.
 \quad}
 \tag{4.5}
\]
例如完整 Wiener 尾直接由几何级数给
\[
 \sum_{|k|>K}|\widehat{\widetilde v_0}(4k)|
 \le\frac{2M e^{-4s_\psi(K+1)}}{1-e^{-4s_\psi}}.
 \tag{4.6}
\]
没有从这些较保守的全复模数声称某个低 \(K\) 已有很小尾；若用于
实际有限 Schur 列，必须代入真实所需的 \(K\) 和费用。

## 5. 含均值的有限秩共根剪切正则化

R53/R85 的 canonical root 频率记为
\(\Gamma(j)=q|j|\)（\(j\ne0\)），\(\Gamma(0)=1\)。
regular 有限端口仍单独保留，以下剪切只作用于 root 角空间。
对 \(L_*=2048\) 置
\[
 \Gamma_*=\max(\Gamma,L_*),\qquad
 P_{0,*}=\Gamma_*^{-1}M_{\widetilde v_0}\Gamma_*^{-1}.
 \tag{5.1}
\]
它是实际实自伴算子，根零模没有删除。取 root balanced
\(Q=\Gamma^{1/3}\)，则
\[
 \|Q P_{0,*}Q\|
 \le M L_*^{-4/3}<.230857937.
 \tag{5.2}
\]
这是逐点最大值
\(\sup_{\gamma\ge1}\gamma^{1/3}/\max(\gamma,L_*)=L_*^{-2/3}\)
和乘法算子 \(L^2\) norm 的直接结果。

R39 的完整 balanced 根 Airy frame 在非零频率的四个常数由
\(\operatorname{Ai}(0),\operatorname{Bi}(0),
\operatorname{Ai}'(0),\operatorname{Bi}'(0)\) 给出。
由准确 Gamma 初值，Arb 直接验证
\[
 \operatorname{Ai}(0)^2+\operatorname{Bi}(0)^2+
 \operatorname{Ai}'(0)^2+\operatorname{Bi}'(0)^2<1.
 \tag{5.3}
\]
记 \(c=c_A^{-1/2}\)。非零块用 Frobenius norm 及准确
\(|\det F|=2c^2/\pi\)，零模块直接计算奇异值，统一得
\[
 \|\overline F_*(0)\|\le\sqrt2c,\qquad
 \|\overline F_*(0)^{-1}\|\le\frac{\pi}{\sqrt2c}.
 \tag{5.4}
\]
regular 有限端口可用同一零模块 convention，并保持 R85 的同一
通量因子 \(c_J\)。于是新根剪切在完整波槽中的正逆 norm 均至多
\[
              1+\pi\|QP_{0,*}Q\|<1.725261598.
 \tag{5.5}
\]
这个费用由实际报告
notes/2026-11-12-actual-root-regularized-shear-budget.json 支付；
源为 scripts/fourfold_phase_root_shear_regularized_budget.py。

必须保留它与原始 \(P_0=\Gamma^{-1}M_{\widetilde v_0}\Gamma^{-1}\)
之间的准确差。令 \(D=\Gamma^{-1}-\Gamma_*^{-1}\)，则
\[
 P_0-P_{0,*}
       =D M_{\widetilde v_0}\Gamma^{-1}
                 +\Gamma_*^{-1}M_{\widetilde v_0}D.
 \tag{5.6}
\]
只有 \(\Gamma<L_*\) 的有限模出现在 \(D\) 中。由当前 \(q_-\)，
四重整数索引至多 \(|k|\le61\)，根低空间维数至多 123，
所以 (5.6) 的秩至多 246。其矩阵并非只占一个有限方块：
它含全部低行或低列及其高频尾。必须把这些真实有限秩列/行
加入完整 Schur，或者用 (4.5) 对实际截断补齐全部尾。
本节只支付一个条件数受控的准确根 frame，未证明新增有限
Schur 块可逆，也没有把 regular 平均通量或根均值耦合删掉。
