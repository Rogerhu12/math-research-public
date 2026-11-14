# R90：实际投影高角边界延拓、压缩整帽 contact 与 regular 源

2026-11-12，independent-audit。

**状态：完整证明，当前 55 格真实领口与 R89 全正体区的常数已实际支付。**
本篇把 R89 的物理高角体 coercivity 接到真正的边界延拓。先沿实际
shear 构造延拓，再施加固定物理 Fourier 投影；完整计算二者不交换的
费用。所得 Poisson、普通体源和 regular Robin 源界属于整个真实
正帽的高角限制问题。它们不等于未压缩整帽的全部输出；完整低高
Schur、根低模、regular 平均值和平均通量始终保留。

## 1. 对象与空间

采用 R89 的同一准确参数盒、真实根和物理密度 \(dx\,d\theta\)：
\[
 \delta_5=-7789843107295549/4611686018427387904,\quad
 |\delta-\delta_5|\le1/2500000,\qquad x=r-t(\delta).
 \tag{90.1}
\]
设 \(L=25/8-t\)，\(l=1/4-t\)。真实正 form 为 R89(89.2)
\[
 b(u,u)=\int_0^L
       \alpha|D u|^2+\eta K_0|u_\theta|^2
       +\langle\Gamma_Hu(L),u(L)\rangle,\qquad
 D=\partial_x-q\partial_\theta.
 \tag{90.2}
\]
角积分在 \(d\theta\) 中，尾是 R74 同一个完整真实尾。
令 \(P=P_N\) 保留四重模 \(e^{4ik\theta}\) 中
\(|k|\ge N+1\)，并置
\[
 \lambda_N=4(N+1),\qquad \nu_N=4N.
 \tag{90.3}
\]
根高角 trace norm 精确定义为
\[
       \|a\|_{X_N}=\||D_\theta|^{1/3}a\|_2,\qquad Pa=a.
 \tag{90.4}
\]
其对偶是同一个高角子空间上的齐次 \(H^{-1/3}\)。
因为这里没有零频率，该定义无奇点。原来的根零模与 regular
\(\xi,\lambda\) 两槽仍在完整低系统中，并未被全局删除。

R89 给高角 form 域上的实际常数
\[
 b(u,u)\ge\kappa_N\|u\|_2^2,\qquad
 \kappa_N=\frac{m_0}{3}
     \left(\lambda_N^{4/3}-\tfrac32Q^2\right),
 \tag{90.5}
\]
同时保留有限长度条件。下文只使用已经严格验证
\(\kappa_N>0\) 的 \(N\)。

## 2. 真 shear 延拓与完整物理投影交换项

在真实领口 \(0\le x\le l\) 内，用 R66 的根锚定角图
\(\varphi(x,\theta)\)，满足
\[
 D\varphi=0,\qquad \varphi(0,\theta)=\theta.
 \tag{90.6}
\]
它是已证明存在的实际圆周微分同胚。令 \(J_c\) 为
\(\varphi_\theta\) 及其倒数的公共上界。当前证书取
\(J_c<1.276240798\)。

对高角根数据 \(a\) 定义在 shear 坐标中的延拓
\[
 v(x,\varphi)=\sum_{|k|>N}
          (1-x/h_k)_+a_k e^{4ik\varphi},\qquad
 h_k=\min\{l,|4k|^{-2/3}\},
 \tag{90.7}
\]
并令 \(E a(x,\theta)=v(x,\varphi(x,\theta))\)，在 \(x\ge l\)
准确延为零。随后取
\[
                          E_Na=P E a.
 \tag{90.8}
\]
根迹准确为 \(a\)，regular 端迹准确为零，且每个物理截面
\(P E_Na=E_Na\)。实际剪切一般不保持 Fourier 子空间；(90.8)
不是省略这一步的记号。

取领口内的实际界
\[
 Q_0\ge\|q\|_\infty,\qquad Q_1\ge\|q_\theta\|_\infty.
 \tag{90.9}
\]
令 \(P_{\rm lo}=I-P\)。由角分部，
\[
 \begin{split}
 P_{\rm lo}(q u_\theta)
 &=\partial_\theta P_{\rm lo}(qu)-P_{\rm lo}(q_\theta u),\\
 \|P_{\rm lo}(q u_\theta)\|_2
 &\le(\nu_N Q_0+Q_1)\|u\|_2,\\
 \|q\,\partial_\theta P_{\rm lo}u\|_2
 &\le\nu_N Q_0\|u\|_2.
 \end{split}
 \tag{90.10}
\]
因此真正的交换项满足
\[
 \boxed{\quad
 \|[P,q]\partial_\theta\|_{L^2\to L^2}
 \le C_N:=2\nu_NQ_0+Q_1=8NQ_0+Q_1.
 \quad}
 \tag{90.11}
\]
这个界保留所有低行、高列和相反的耦合，没有假定 \(Pq=qP\)。
而且
\[
                     D P E=P D E+[P,q]\partial_\theta E.
 \tag{90.12}
\]

## 3. 实际高角延拓的完整能量费

定义真正的物理领口系数上界
\[
 M_{\rm ph}\ge
      \sup\max\{\alpha,\eta K_0/x\}.
 \tag{90.13}
\]
R66 报告中的 \(M_c\) 正是使用
\[
                         M_c=M_{\rm ph}J_c
 \tag{90.14}
\]
这一安全聚合；下文使用该已支付的乘积，不把一个任意 shear
矩阵上界免费当作物理系数界。

换元 \(d\theta=d\varphi/\varphi_\theta\)，由 \(D E=v_x\)，
\[
 \|D E\|_2^2\le J_c\|v_x\|_2^2,\quad
 \int x|E_\theta|^2\le J_c\int x|v_\varphi|^2,\quad
 \|E\|_2^2\le J_c\|v\|_2^2.
 \tag{90.15}
\]
对每个模直接积分 ramp 得
\[
 \int|v_k'|^2=h_k^{-1}|a_k|^2,\quad
 \int x|4k|^2|v_k|^2=\tfrac1{12}|4k|^2h_k^2|a_k|^2,\quad
 \int|v_k|^2=\tfrac13h_k|a_k|^2.
 \tag{90.16}
\]
置
\[
 d_N=\max\{1,(l_-\lambda_N^{2/3})^{-1}\},\qquad
 u_N=\frac{C_N}{\sqrt3\,\lambda_N^{2/3}}.
 \tag{90.17}
\]
于是
\[
 \|v_x\|_2^2\le d_N\|a\|_{X_N}^2,\quad
 \int x|v_\varphi|^2\le\tfrac1{12}\|a\|_{X_N}^2,\quad
 \|v\|_2^2\le\tfrac13\lambda_N^{-4/3}\|a\|_{X_N}^2.
 \tag{90.18}
\]
投影与角导数、乘 \(x\) 交换。对 (90.12) 用
\(|A+B|^2\le(1+\varepsilon)|A|^2+
(1+\varepsilon^{-1})|B|^2\)，结合 (90.13)—(90.18)，得到
\[
 b(E_Na,E_Na)
 \le M_c\left[(1+\varepsilon)d_N+\tfrac1{12}
                 +(1+\varepsilon^{-1})u_N^2\right]\|a\|_{X_N}^2.
 \tag{90.19}
\]
regular Robin 项准确为零，因为整个延拓支撑于根领口。
取 \(\varepsilon=u_N/\sqrt{d_N}\)，零交换项的情形取极限，得
\[
 \boxed{\quad
 b(E_Na,E_Na)\le E_N^{\rm en}\|a\|_{X_N}^2,\qquad
 E_N^{\rm en}=M_c\left[(\sqrt{d_N}+u_N)^2+\tfrac1{12}\right].
 \quad}
 \tag{90.20}
\]
所有 ramp 只作为自然 form 域中的 \(H^1\) 延拓，不是一个冒称
\(C^2\) 的几何修正。有限长度截断已完整包含在 \(d_N\) 中；
不要求 \(\lambda_N^{-2/3}\le l\)。

## 4. 真正限制整帽的 Poisson、体源和高根 contact

在每个物理截面约束 \(Pu=u\)，并施加根迹 \(a\)。
(90.8) 支付 trace onto，R89 支付齐次根迹空间 coercivity，
所以存在同一完整正帽上的唯一压缩调和解 \(H_Na\)。
它在整个 \([0,L]\) 上最小化真实 form，因而
\[
 b(H_Na,H_Na)\le b(E_Na,E_Na).
 \tag{90.21}
\]
用 (90.5) 得
\[
 \boxed{\quad
 \|H_N:X_N\to L^2(dx\,d\theta)\|
 \le C_N^{\rm cont}:=
             \sqrt{E_N^{\rm en}/\kappa_N}.
 \quad}
 \tag{90.22}
\]
Green 恒等式在同一个限制域给高根 contact
\(K_N=-H_N^*\)。对完整普通体源 \(f\in L^2\)，
\[
                  \|K_Nf\|_{X_N^*}\le
                       C_N^{\rm cont}\|f\|_2.
 \tag{90.23}
\]
该解只要求对高角 test function 调和。一般仍有非零低角体残差
和低根通量；这些是实际 Schur cross。尤其
\(\Lambda_N\) 不是未经说明的 \(P\Lambda_{\rm full}P\)，
(90.23) 不能改称完整未压缩帽的全部 contact 界。

限制 DN 是正自伴，且
\[
 0\le\Lambda_N\le E_N^{\rm en}
          \quad\hbox{作为 }X_N\to X_N^*\hbox{ 的二次型}.
 \tag{90.24}
\]
因此其 balanced Cayley 是实际高角 Hilbert 空间上的 onto
unitary。这个结论仍属于限制问题，不能用它绕过完整低高反馈。

## 5. 真正 regular Robin 源

R74 的真实外尾在物理非零模上满足
\[
            \gamma_n\ge(1-2^{-36})\frac{|n|}{4\omega}
                         >\frac{|n|}{7},\qquad \omega<3/2.
 \tag{90.25}
\]
因此对高角 \(u\)
\[
       \||D_\theta|^{1/2}u(L)\|_2^2\le7\,b(u,u).
 \tag{90.26}
\]
给定 regular 高角 Robin 负荷 \(g\)，采用物理齐次
\(H^{-1/2}\) norm，其弱线性泛函是准确
\(\langle g,u(L)\rangle\)。高角解因此满足
\[
 b(u,u)^{1/2}\le\sqrt7\|g\|_{H^{-1/2}},\qquad
 \|u\|_2\le\sqrt{7/\kappa_N}\|g\|_{H^{-1/2}}.
 \tag{90.27}
\]
与 \(H_Na\) 的 Green 配对给 root contact
\[
       \|K_{N,\rm reg}g\|_{X_N^*}
       \le\sqrt{7E_N^{\rm en}}\|g\|_{H^{-1/2}}.
 \tag{90.28}
\]
非齐次真实尾转换中的 \(J,R_m\) 等实际源迹须先按 R74 形成这个
物理 \(g\)，不能删去。regular 均值负荷及 \(\xi,\lambda\)
是另一组真实低槽，(90.25) 不含零模，因而没有用它们作虚假的
零模 Robin 逆。

## 6. 当前连续参数族的实际数值

源 scripts/fourfold_phase_physical_high_boundary_budget.py 从同一
完成的 55 个领口格重算
\[
           Q_0<1.005959366,\qquad Q_1<21.021821602,
 \tag{90.29}
\]
并读取同一 \(\delta_5\pm4\,10^{-7}\) 盒的 R89 全体界。
每个输入 SHA、参数包含关系以及实际整帽关系均检查。输出为
notes/2026-11-12-actual-physical-high-boundary-budget.json。

| \(N\) | 真投影延拓能量 \(E_N^{\rm en}\) 上界 | 压缩体源/高根 contact \(C_N^{\rm cont}\) 上界 |
|---:|---:|---:|
| 32 | 2925.373524 | 199.101045 |
| 64 | 3719.710196 | **21.596427** |
| 128 | 5090.111432 | 13.527447 |
| 256 | 7429.862289 | 9.777196 |
| 512 | 11334.722505 | 7.465540 |
| 1024 | 17461.324225 | 5.795664 |

完整报告还给 regular 负荷的 (90.27)、(90.28) 费用。该改进明确
属于物理高角限制问题：R87 的 canonical Airy 输入仍须支付真实
角/height/frame 转换，低角/高角 coupling 由完整 Schur 保持。
本篇未宣称完整 Airy 余项、有限 Schur 可逆或非线性零解已经完成。
