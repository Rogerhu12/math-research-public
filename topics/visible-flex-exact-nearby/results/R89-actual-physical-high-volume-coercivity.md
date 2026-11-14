# R89：实际物理高角体块的有限区间 coercivity 与 Schur 源费

2026-11-12，independent-audit。

**状态：完整证明，当前准确参数族的全部正体区常数由已完成逐格数据重新聚合。**
本篇直接在当前真实物理角 \(\theta\) 中压缩高角体块。既不要求
Fourier 投影与实际 drift 交换，也不把半线 Airy 谱界无条件用于有限
区间。结果给出显式的 \(N\) 函数 \(\kappa_N\)、压缩普通体源逆和
Schur 残差费用。它不是完整帽 DN、Poisson 或反射余项的界；
真实均值端口和所有低高耦合继续属于完整系统。

## 1. 同一实际对象、物理密度和端点

参数为共同盒
\[
 \delta_5=-7789843107295549/4611686018427387904,\qquad
 |\delta-\delta_5|\le1/2500000.
 \tag{89.1}
\]
每个参数使用自己的真实根 \(t=t(\delta)\)，令
\[
 x=r-t,\qquad L=25/8-t.
\]
在 R69 已完成的整个正体区和 natural graft 上，R37 的真实
ground-state 变换 \(w=Y_z u\) 给正 form
\[
 \begin{split}
 b(u,v)={}&
 \int_0^L\!\!\int_{S^1}
 \alpha (u_x-q u_\theta)
       \overline{(v_x-q v_\theta)}
       +\eta K_0 u_\theta\overline{v_\theta}\,d\theta\,dx\\
 &+\langle\Gamma_H u(L),v(L)\rangle_{d\theta}.
 \end{split}
 \tag{89.2}
\]
这里 \(\alpha,\eta,q\) 是实际物理变量中的 R66/R83 系数，
\(q=M/D\)，测度准确为 \(dr\,d\theta=dx\,d\theta\)。没有先乘一个
未知 Jacobian，也没有把 shear 坐标的矩阵下界误作物理下界。
R74 已构造的整个无限尾给同一物理切口上的
\(\Gamma_H\ge0\)；其常数核只为 form 的定义。

真实 regular 平均值 \(\xi=\langle u(L),\phi_0\rangle\) 和平均
conormal \(\lambda\) 是两个保留的有限槽。对高角体空间两者不被
另设成无条件的整体零模消失结论；它们在低角系统中联立。
根端可以采用自然 form 域，也可以加齐次 Dirichlet 条件
\(u(0)=0\)。下面的体不等式对两个域都成立，因为证明不使用任一
端值为零。若加入其它非负 Robin form，也仍然成立；负边界 form
不能免费套用。

从完整的逐格报告定义真正的物理常数
\[
 m_0\le
 \inf_{x,\theta,\delta}\min\{\alpha,\eta K_0/x\}>0,\qquad
 Q\ge\sup_{x,\theta,\delta}|q_\theta|.
 \tag{89.3}
\]
在 \(x=0\) 使用已证明的可去值 \(K_0/x\)。
这与 R69 的构造完全相同，但尚未除以 shear 的 Jacobian 上界。
因此
\[
 b(u,u)\ge m_0
       \left(\|u_x-q u_\theta\|_2^2+
                   \int x|u_\theta|^2\right).
 \tag{89.4}
\]
所有 \(L^2\) 范数均用上面的物理测度。

## 2. 真半密度输运给 Hilbert 值基本定理

置
\[
 D u=u_x-q u_\theta,\qquad
 \widetilde D u=u_x-q u_\theta-\tfrac12q_\theta u.
 \tag{89.5}
\]
对每个固定 \(x\)，实向量场
\(-q\partial_\theta-\frac12q_\theta\) 在 \(L^2(d\theta)\) 上为
反自伴。它由真实圆周流及其半密度实现；实际 \(q\) 的有限径向
正则和完整角正则已由本对象的各真实 span 及接合给出。有限区间
上存在对应的双向酉传播 \(U(x,s)\)。令
\[
 v(x)=U(0,x)u(x).
\]
在光滑函数上直接微分，并由能量完备化延拓，得到
\[
 \|v(x)\|_{L^2_\theta}=\|u(x)\|_{L^2_\theta},\qquad
 v'(x)=U(0,x)\widetilde D u(x).
 \tag{89.6}
\]
这只为证明体能量式使用实际 unitary transport，不需要数值计算
该流，不声称 Fourier 投影在此流下保持不变。

## 3. 有限区间比较：明确保留长度条件

设 \(v:[0,L]\to\mathcal H\) 为任意 Hilbert 值 \(H^1\) 函数，
\(0<h\le L/2\)。则
\[
 \int_0^L\|v\|^2
 \le 3\int_h^L\|v\|^2+
                   2h^2\int_0^{2h}\|v'\|^2.
 \tag{89.7}
\]
**证明。** 对 \(0\le x\le h\le y\le2h\)，
\[
 \|v(x)\|^2\le
   2\|v(y)\|^2+
   2(y-x)\int_x^y\|v'(z)\|^2\,dz.
 \tag{89.8}
\]
对 \(y\) 取平均再对 \(x\) 积分。交换三重积分后，固定 \(z\) 的
非负核为
\[
 \frac1h\int_0^{\min(h,z)}
           \int_{\max(h,z)}^{2h}(y-x)\,dy\,dx
 \le h^2.
 \tag{89.9}
\]
当 \(0\le z\le h\) 时左边为
\(3hz/2-z^2/2\)；当 \(h\le z\le2h\) 时为
\(h^2+hz/2-z^2/2\)。二者都不超过 \(h^2\)。于是
\(\int_0^h\|v\|^2\le2\int_h^{2h}\|v\|^2+
2h^2\int_0^{2h}\|v'\|^2\)，加上 \([h,L]\) 即得 (89.7)。
没有假定 \(v(0)\)、\(v(L)\) 为零，也没有借用半线边界谱。

令 \(P_N\) 为物理四重 Fourier 模 \(e^{4ik\theta}\) 中
\(|k|\ge N+1\) 的投影，并置
\[
 \lambda_N=4(N+1).
 \tag{89.10}
\]
若对几乎每个 \(x\)，\(P_Nu(x)=u(x)\)，则
\(\|u_\theta(x)\|_2\ge\lambda_N\|u(x)\|_2\)。
取 \(h=\lambda_N^{-2/3}\)，要求
\[
                    \lambda_N^{-2/3}\le L/2.
 \tag{89.11}
\]
将 (89.6) 代入 (89.7)，并在 \(x\ge h\) 用 \(x\ge h\)，得到
\[
 \lambda_N^{4/3}\|u\|_2^2
 \le 2\|\widetilde D u\|_2^2+
                             3\int x|u_\theta|^2.
 \tag{89.12}
\]
Fourier 高角条件只对原来的 \(u\) 使用，未在酉变换后的 \(v\)
上假设同一个高角条件。

## 4. 显式 \(\kappa_N\) 与压缩普通体源

由 (89.5) 和带参数的平方不等式，
\[
 \|\widetilde D u\|_2^2
 \le\tfrac32\|D u\|_2^2+\tfrac34Q^2\|u\|_2^2.
 \tag{89.13}
\]
结合 (89.4)、(89.12)，得到
\[
 \boxed{\quad
 b(u,u)\ge\kappa_N\|u\|_2^2,\qquad
 \kappa_N=\frac{m_0}{3}
       \left(\lambda_N^{4/3}-\frac32Q^2\right).
 \quad}
 \tag{89.14}
\]
这是完整非径向 drift 的估计；不要求 \(q\) 或 \(q_\theta\) 小。
须同时检查 (89.11) 和 \(\kappa_N>0\)。

令 \(V_N\) 为真实 form 域中满足 \(P_Nu=u\) 的闭子空间；
或者在它上面再加真实根端齐次 Dirichlet 条件。限制真实 form
得到 \(\mathcal A_{HH}\)。对 \(f\in L^2\)，当 (89.11)、
\(\kappa_N>0\) 时，Lax--Milgram 与 (89.14) 给
\[
 \begin{gathered}
 b(u,v)=\langle f,v\rangle\quad(v\in V_N),\\
 \boxed{\quad
 \|u\|_2\le\kappa_N^{-1}\|f\|_2,\qquad
 b(u,u)^{1/2}\le\kappa_N^{-1/2}\|f\|_2.
 \quad}
 \tag{89.15}
 \end{gathered}
\]
form 的梯度完备性来自同一 R69/R74 正实现；(89.14) 额外控制
质量项，所以 restriction 的能量 norm 完整且 coercive。
\(P_N\) 不必与 \(q\)、\(\alpha\) 或 \(\eta\) 交换。

完整低高分解也不需要一个未经证明的投影不变性：低角投影只有
有限多个角模，\(\partial_x P_{\rm low}u\) 可写成
\(P_{\rm low}D u+P_{\rm low}(q u_\theta)\)。后一项按角分部后只含
\(q_\theta u\) 和有限频率乘 \(qu\)，故在自然 form 域上有界。
低角空间仍有完整径向函数自由度；它不因为角模数有限就自动成为
已经认证的有限矩阵。

## 5. 完整 Schur 中可直接使用的源费

若真实弱算子按上述域分解写成
\[
 \begin{pmatrix}
 \mathcal A_{LL}&\mathcal A_{LH}\\
 \mathcal A_{HL}&\mathcal A_{HH}
 \end{pmatrix},
 \tag{89.16}
\]
则完整 Schur correction 为
\[
             \mathcal A_{LH}\mathcal A_{HH}^{-1}\mathcal A_{HL}.
 \tag{89.17}
\]
本篇不把其中任何 cross 设为零。特别是 \(P_Nq\ne qP_N\) 产生的
真实低高项和 regular 的 \(\xi,\lambda\) 行仍在低块中。

对一组实际 trial，若其高块残差已**准确**表示成纯 \(L^2\) 体源
算子 \(F:\mathbb C^d\to L^2\)，则
\[
 0\le F^*\mathcal A_{HH}^{-1}F
       \le\kappa_N^{-1}F^*F.
 \tag{89.18}
\]
逐向量代入 (89.15) 或由正谱序立即证明该式。它可接 R88 的
primal/dual complementary energy 包络，用于真实高角体残差。
若 trial 在根或 regular 端还留下 conormal/Robin 残差，残差泛函
就不是纯 \(L^2\) 体源；必须连同该端的实际 trace norm 一起支付，
不能把它藏进 (89.18)。非齐次 \(\operatorname{div}j=f\) 同样保留
所有真实通量条件。

## 6. 当前 1423 格的实际支付和明确范围

实现位于
scripts/fourfold_phase_physical_high_energy_budget.py，输出为
notes/2026-11-12-actual-physical-high-energy-budget.json。
它逐一核对 R69 的全部输入 SHA、完成标记、准确参数包含关系和
从公共根包络到 \(25/8\) 的 Fraction 无缝覆盖，重算
\(\min(\alpha,\eta K_0/x)\) 与 \(\max|q_\theta|\)。55 个 root
collar 格、1304 个 regular body 格和 64 个 natural graft 格全含在内。
尾只通过同一 R74 已证明为非负的真实 Robin form 接入。

实际有向重聚合给出

- 物理下界 (m_0>0.0240080178498917)；
- 全域 drift 角导数 (Q<21.0218216015248)；
- 全部有限区间长度门成立，公式首次严格给出正数的是 (N=32)，
  即保留物理频率至少 132。这是本充分公式的阈值，不是实际谱的
  最小可逆阈值。

报告中安全向外放宽的部分数值如下。

| (N) | 首个物理频率 | \(\kappa_N\) 下界 | 纯 (L^2) 体源逆上界 |
|---:|---:|---:|---:|
| 32 | 132 | 0.07379624 | 13.550826 |
| 64 | 260 | 7.97526860 | 0.125387627 |
| 128 | 516 | 27.81606281 | 0.035950451 |
| 256 | 1028 | 77.72347187 | 0.012866127 |
| 512 | 2052 | 203.37075489 | 0.004917128 |
| 1024 | 4100 | 519.84138304 | 0.001923664 |

每个数值均来自同一个完整参数盒和全部 1423 个连续几何格，不是
节点采样。报告同时保存达到最坏物理下界和最大 drift 的准确格、
所有源文件 SHA，以及每个 (N) 的有向长度门和逆界。

本篇仅为压缩体块支付 coercivity。把 (89.15) 升级成边界
Poisson/contact 还需真高角边界延拓及完整范数转换。尤其不能把
一个经过 shear 传播的边界延拓无条件投回物理高角空间后，忽略
投影产生的低高耦合。R87 的完整 collar 源、R88 的有限低块及
其它组件的真实传输仍分别保持其已经支付的范围。
