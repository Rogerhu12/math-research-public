# R91：Airy 参数解析因子化与实际完整源预算

2026-11-12，independent-audit。

**状态：完整证明，R87 同一实际领口的全部 56 项源和明确 cutoff 已有向聚合。**
本篇不用每一个 Fourier lag 的二阶角导数估计，而把 Airy 自变量的
非径向变化展开成收敛的乘子与对角算子之和，只需系数的一阶角导数。
这是完整矩阵强界，不是把逐列范数当成算子范数。

实际界仍很大，**没有得到可计算的全反馈 cutoff**。完整记录把
损失定位在当前窄 cutoff 及 R87 系数包络的相消损失。扩大实际正侧
领口、收紧系数以及完整低高耦合仍须支付。

## 1. 空间与同一个真实输入

使用 R87 的准确参数盒、根、无限原函数及有限 canonical 坐标：
\[
 |\delta-\delta_5|\le1/2500000,\qquad
 0\le s=r-t(\delta)\le h=1/2048,\qquad y=s\,a(s,\theta).
 \tag{91.1}
\]
同一完成的 178 格证明
\[
 .98306302<a<1.00270771,\qquad
 .055953798<\phi_\theta<.288068627.
 \tag{91.2}
\]
记 \(\ell\) 为 canonical 圆长，\(q=2\pi/\ell\)，真实频率
\(\lambda_j=4q|j|\)。在 \(L^2(d\phi)\) 中使用正交归一 Fourier
基，所有 Sobolev 范数用真实 \(D_\phi\)，并令
\(\mathcal L=(1+D_\phi^2)^{1/2}\)。
输出源范数为 R85 的
\[
                     L^2(ds;H^{-2/3}(d\varphi)),
 \tag{91.3}
\]
其中 \(\varphi\) 是根锚定的真实物理 shear 角，周期 \(2\pi\)。
输入 \(P^{\rm can}_{>N}\) 是 canonical 四重模 \(|j|>N\)，与 R89 的
物理 \(\theta\) 投影不同。输入零模和 regular 有限槽继续按 R85
取零 trial；实际反射在这些槽中未设为 \(-I\)。非零输入产生的全部
输出频率、均值和两符号都保留。

## 2. 复 Airy 参数的明确统一包络

设
\[
 R=\frac14,\quad \gamma=\frac78,\quad
 c_*=\gamma(1-R)-\frac{\gamma^3}{3}-\frac{R^2}{4\gamma}
       =\frac{4463}{10752}>0.
 \tag{91.4}
\]
对 \(z\ge0,\ |b-1|\le R\)，有
\[
 \boxed{\quad
 |\operatorname{Ai}(bz)|,\ |\operatorname{Ai}'(bz)|
 \le B(z):=\frac32(1+z)e^{-c_*z^{3/2}}.
 \quad}
 \tag{91.5}
\]

**证明。** 标准 contour
\[
 \operatorname{Ai}(w)=\frac1{2\pi i}
 \int_{\infty e^{-i\pi/3}}^{\infty e^{i\pi/3}}e^{t^3/3-wt}\,dt
 \tag{91.6}
\]
可移到 \(t=\gamma\sqrt z+iu\)。被积函数整；连接弧上
\(\Re(t^3)\le0\)，靠近竖直端点时固定正实部还给负二次项，
故截断弧积分趋于零，竖直积分及其 \(w\) 导数绝对收敛。
对 \(w=bz\) 完成平方，
\[
 \Re(t^3/3-wt)\le-c_*z^{3/2}
 -\gamma\sqrt z\left(u-\frac{\Im b\,\sqrt z}{2\gamma}\right)^2 .
 \tag{91.7}
\]
高斯积分给
\[
 \begin{split}
 |\operatorname{Ai}(bz)|
 &\le\frac{z^{-1/4}}{2\sqrt{\pi\gamma}}e^{-c_*z^{3/2}},\\
 |\operatorname{Ai}'(bz)|
 &\le\left[
 \frac{\gamma+R/(2\gamma)}{2\sqrt{\pi\gamma}}z^{1/4}
 +\frac1{2\pi\gamma}z^{-1/2}\right]e^{-c_*z^{3/2}}.
 \end{split}
 \tag{91.8}
\]
当 \(z\ge1\)，两式都小于 (91.5)。

对 \(0\le z\le1\)，\(|bz|\le5/4\)。由 Airy 方程和
\(|\operatorname{Ai}(0)|,|\operatorname{Ai}'(0)|<1/2\)，绝对
Maclaurin 系数由 \(F''=xF,\ F(0)=F'(0)=1/2\) 控制。其正系数满足
\[
 a_0=a_1=1/2,\quad a_2=0,\qquad
 a_{n+3}=a_n/((n+3)(n+2)).
 \tag{91.9}
\]
在 \(x=5/4\) 保留到次数 \(20\) 后，三同余类从次数 \(21\) 起，
函数及导数的连续项比均小于 \(1/100\)。准确有理加总给
\[
 F(5/4)<1.406,\qquad F'(5/4)<1.297<3/2.
 \tag{91.10}
\]
程序保存完整有理上界。又因
\(\log(1+z)\ge z/2\ge c_*z^{3/2}\)，(91.5) 在该区间也成立。
初值 Gamma 表达式由 256-bit Arb 另行确认小于 \(1/2\)。

对 \(b\) 用 Cauchy 公式，\(d=0,1,n\ge0\) 时
\[
 \left|\frac{z^n}{n!}\operatorname{Ai}^{(d+n)}(z)\right|
                      \le R^{-n}B(z).
 \tag{91.11}
\]
无需为每个 \(n\) 重新累积高阶 Airy 导数多项式。
标准 contour、方程及初值的 primary 来源是
[DLMF 9.5.4](https://dlmf.nist.gov/9.5.E4) 和
[DLMF 9.2.1、9.2.3–4](https://dlmf.nist.gov/9.2)；
统一常数及以下算子估计由本篇推导给出。

## 3. 一个角导数的完整乘子费用

在固定圆长的真实物理角中，若
\(\|c\|_\infty\le C_0,\ \|c'\|_\infty\le C_1\)，则
\[
 \|M_c\|_{H^{-t}\to H^{-t}}
 \le\mathfrak m_t(C_0,C_1)
 :=C_0^{1-t}(C_0+C_1)^t,\qquad0\le t\le1.
 \tag{91.12}
\]
在 \(L^2\) 的界是 \(C_0\)；对函数与一阶导数的二元向量用乘法法则，
\(H^1\) 界为 \(C_0+C_1\)。Hilbert 尺度插值和对偶即得 (91.12)，
也适用于复乘子。

设 \(\epsilon=a-1\)，在每个固定 \(s\) 的真实 \(\phi\) 圆上有
\[
 \|\epsilon\|_\infty\le d_0<R,\qquad
 \|\partial_\phi\epsilon\|_\infty\le d_1.
 \tag{91.13}
\]
于是
\[
 \|M_{\epsilon^n}\|_{H^{-t}\to H^{-t}}
 \le d_0^n(1+nd_1/d_0)^t.
 \tag{91.14}
\]
置 \(\rho=d_0/R\)。对几何概率分布
\((1-\rho)\rho^n\) 用凹函数 \(x^t\)，得到
\[
 \boxed{\quad
 \sum_{n\ge0}\rho^n(1+nd_1/d_0)^t
 \le G_t:=\frac1{1-\rho}
      \left(1+\frac{d_1}{d_0}\frac{\rho}{1-\rho}\right)^t.
 \quad}
 \tag{91.15}
\]
若 \(d_0=0\)，真实 \(\epsilon\) 恒零，仅有 \(n=0\) 项。

## 4. 强算子因子化，保全部 Fourier 行

考虑
\[
 (Ta)(s,\phi)=c(s,\phi)s^k
   \sum_{j\ne0}\lambda_j^p
   \operatorname{Ai}^{(d)}(a(s,\phi)s\lambda_j^{2/3})
       a_j e_j(\phi),\qquad d=0,1.
 \tag{91.16}
\]
符号 \(i\,\operatorname{sgn}j\) 保留在输入对角酉算子中，不增加费用。
在 \(z=s\lambda_j^{2/3}\) 展开，准确有
\[
 T=\sum_{n\ge0}M_cM_{\epsilon^n}A_n,\qquad
 (A_n)_j=s^k\lambda_j^p
             \frac{z^n\operatorname{Ai}^{(d+n)}(z)}{n!}.
 \tag{91.17}
\]
每个 \(A_n\) 是全圆对角算子。先对有限 Fourier 数据用解析恒等式，
再由 (91.11)—(91.15) 证明算子 norm 绝对收敛，便得真实 \(L^2\)
延拓。乘子可产生任意输出频率，包括均值及相反频率。

设输入频率 \(\lambda_j\ge\Lambda>0\)，并令
\[
 t=2/3,\qquad e=2k/3-p-1,\qquad q_1=p+4/3.
 \tag{91.18}
\]
用 \(\langle\lambda\rangle^2\le(1+\Lambda^{-2})\lambda^2\) 和
\(\langle\lambda\rangle^{-2/3}\le\lambda^{-2/3}\)，Parseval、Tonelli 给
\[
 \boxed{\quad
 \|T\mathcal L^2P^{\rm can}_{>N}\|_{L^2\to L^2_sH^{-2/3}_\phi}
 \le(1+\Lambda^{-2})\mathfrak m_{2/3}(C_0,C_1)
                        G_{2/3}\mathcal D_{k,p}(\Lambda).
 \quad}
 \tag{91.19}
\]
这里先对固定 \(n,s\) 用统一乘子 norm，再对对角 Fourier 平方和
积分，未非法移动未知径向积分中的 \(\sup_j\)。

定义准确矩
\[
 \mathcal M_k(d)=\frac32
 \left[\frac23\sum_{\nu=0}^2 b_\nu
       d^{-2(2k+\nu+1)/3}
       \Gamma\!\left(\frac{2(2k+\nu+1)}3\right)\right]^{1/2},
 \quad (b_0,b_1,b_2)=(1,2,1).
 \tag{91.20}
\]
它是 \(\frac32z^k(1+z)e^{-dz^{3/2}/2}\) 的半线 \(L^2\) norm。
若 \(e>0\)，
\[
 \mathcal D_{k,p}(\Lambda)\le\mathcal M_k(2c_*)\Lambda^{-e}.
 \tag{91.21}
\]
为避免过早把真实有限领口放大成半线，另置
\[
 S(r)=\sup_{z\ge0}z^re^{-c_*z^{3/2}}
 =\left(\frac{2r}{3\mathrm e c_*}\right)^{2r/3}\ (r>0),\quad S(0)=1.
 \tag{91.22}
\]
若 \(q_1\ge0\)，逐 \(s\) 最大化再积分给
\[
 \mathcal D_{k,p}(\Lambda)\le
 \frac32[S(3q_1/2)+S(3q_1/2+1)]\frac{h^{3e/2}}{\sqrt{3e}}.
 \tag{91.23}
\]
若 \(q_1<0\)，可用
\[
 \mathcal D_{k,p}(\Lambda)\le
 \frac32[1+S(1)]\Lambda^{q_1}\frac{h^{k+1/2}}{\sqrt{2k+1}}.
 \tag{91.24}
\]
程序取独立有效界的较小者。

对支撑在 \(s\ge s_0>0\) 的 cutoff 项，允许 \(e\le0\)。从平方指数
分出一半后，
\[
 \mathcal D^{\rm tail}_{k,p}(\Lambda)
 \le\mathcal M_k(c_*)\sup_{\lambda\ge\Lambda}
          \lambda^{-e}e^{-b\lambda},\quad b=\tfrac12c_*s_0^{3/2}.
 \tag{91.25}
\]
一元最大值在 \(\Lambda\) 或 \(-e/b\) 处取得。对 \(q_1\ge0\)，另可用
\[
 \frac32[S(3q_1/2)+S(3q_1/2+1)]
       \left(\int_{s_0}^h s^{2k-3q_1}\,ds\right)^{1/2}.
 \tag{91.26}
\]
指数为 \(-1\) 时用对数；下端严格正，所有这些有限负幂可积。
\(q_1<0\) 仍可用 (91.24)。

## 5. 完整物理密度及两个实际角图

固定物理 \(s\)，令
\[
 \phi=H_s(\varphi),\quad H_s'=\phi_\theta/\varphi_\theta,\quad
 z=J/(\tau\phi_\theta).
 \tag{91.27}
\]
R87 的 grounded 物理源是
\(f_\theta=(J/\tau)f_{\rm can}\circ\Psi\)；换到 R85 shear 角后恰为
\[
                   f_\varphi=H_s'(zf_{\rm can})\circ H_s.
 \tag{91.28}
\]
程序先将 \(z\) 乘入每项系数，再用这个密度拉回，未省略 Jacobian。

若 \(0<b_-\le H_s'\le b_+\)，密度拉回 \(L^2\) norm 至多
\(\sqrt{b_+}\)。它与 \(v\mapsto v\circ H_s^{-1}\) 准确对偶，
故 \(H^{-1}\) norm 至多
\(\max\{\sqrt{b_+},b_-^{-1/2}\}\)。插值得
\[
 \|f\mapsto H_s'f\circ H_s\|_{H^{-2/3}\to H^{-2/3}}
 \le b_+^{1/6}\max\{\sqrt{b_+},b_-^{-1/2}\}^{2/3}.
 \tag{91.29}
\]
由 R66 实际 shear 导数及逆导数界，可取
\[
 b_-=\phi_{\theta,-}/1.276240798,\qquad
 b_+=1.276240798\,\phi_{\theta,+}.
 \tag{91.30}
\]
在每个真实连续角格中，程序使用
\[
 z_0\le\frac{(J/\tau)_0}{\phi_{\theta,-}},\qquad
 |z_\theta|\le\frac{|(J/\tau)_\theta|}{\phi_{\theta,-}}
 +\frac{(J/\tau)_0|\phi_{\theta\theta}|}{\phi_{\theta,-}^2}.
 \tag{91.31}
\]
各系数相乘后才取最坏格，再用
\(\partial_\phi|_s=\phi_\theta^{-1}\partial_\theta\)，不是固定
canonical \(y\) 的角导数。这不要求 mixed radial 坐标有无限角解析性。

## 6. 全源项和一个已支付的实际 cutoff

使用 R87 真实物理多项式 \(B,C\) 及
\[
 U=c\lambda^{-1/3}e^{i\epsilon\lambda\phi}
 [(1+i\epsilon C/\lambda)A+\lambda^{-4/3}BA'],\quad
 c=c_A^{-1/2},\quad A=\operatorname{Ai}(y\lambda^{2/3}).
 \tag{91.32}
\]
除 R87(87.20) 的九分项外，完整主部误差是
\[
 -2E_{12}U_{y\phi}-(E_{12})_yU_\phi-(E_{12})_\phi U_y
                  -E_{22}U_{\phi\phi}-(E_{22})_\phi U_\phi.
 \tag{91.33}
\]
逐项微分并准确用 \(A''=y\lambda^{2/3}A\) 后，
\(U,U_y,U_\phi,U_{y\phi},U_{\phi\phi}\) 各有 \(3,5,5,9,7\) 个
Ai/Ai′ 项；(91.33) 因而有 31 项。程序明列系数、
\(\lambda\) 次数、真实径向消失阶和整数因子，全部相位导数及
\(B,C\) 导数都保留。

明确取
\[
 y_{\rm out}=49h/50,\qquad y_{\rm in}=49h/100,\qquad
 d=y_{\rm out}-y_{\rm in}.
 \tag{91.34}
\]
在二者之间置 \(u=(y-y_{\rm in})/d\) 并令
\[
 \chi(y)=1-10u^3+15u^4-6u^5;
 \tag{91.35}
\]
左侧恒 \(1\)，右侧恒零。它是 \(C^2\)，且
\[
 |\chi|\le1,\quad|\chi'|\le15/(8d),\quad
 |\chi''|\le6/d^2,\quad|\chi'''|\le60/d^3
 \tag{91.36}
\]
在弱导数意义成立。由 (91.2)，\(y_{\rm out}<a_-h\)，所以整个
cutoff 在实际图域内，延为零时没有额外分布源。

因 \(E_{11}=0\)，准确交换项为
\[
 [P_{\rm can},\chi]U=-2\chi'U_y-\chi''U
                    -2\chi'E_{12}U_\phi-\chi'(E_{12})_\phi U.
 \tag{91.37}
\]
它有 16 项，总数 \(9+31+16=56\)，都支撑在
\[
                         s\ge s_0=y_{\rm in}/a_+>0.
 \tag{91.38}
\]
固定 \(s\) 上
\((\chi^{(m)}(y))_\theta=\chi^{(m+1)}(y)y_\theta\)，按 R87 实际
\(y_\theta\) 计费。对 \(\chi\) 乘内部源，还比较
\(\chi S=S+(\chi-1)S\) 的尾支持分解与直接乘子界，取较小者。
未以“指数衰减”省略 (91.37)。

## 7. 实际数字和仍未完成的强逆门

实现为 scripts/fourfold_phase_airy_factorized_source_budget.py，报告
notes/2026-11-12-actual-factorized-airy-source-budget.json。
程序检查 R87 完整准确覆盖、冻结源及依赖 SHA、同一参数对象和
实际 \(q\) 证书，得到安全界
\[
 d_0<.016936976,\quad d_1<2.857108642,\quad
 G_{2/3}<6.009054142,\quad C_{\rm density}<2.400338255.
 \tag{91.39}
\]
因此解析因子化与实际密度费用本身有限且适中。

令 \(K_{\rm trial}(N)\) 为完整 grounded trial 源从
\(L^2_\phi\) 经右乘 \(\mathcal L^2P^{\rm can}_{>N}\) 到 (91.3)
的 norm。所有 56 项加总给：

| canonical \(N\) | \(K_{\rm trial}(N)\) 安全上界 |
|---:|---:|
| 64 | \(2.093\,10^{15}\) |
| 256 | \(2.092\,10^{15}\) |
| 1024 | \(2.091\,10^{15}\) |
| 4096 | \(2.091\,10^{15}\) |
| 16384 | \(2.091\,10^{15}\) |
| 65536 | \(2.090\,10^{15}\) |

报告保存每项费用。最大两项是 \(-2\chi'U_y\) 的 free Ai′ 项和
\(-\chi''U\) 的 free Ai 项。即使去除 cutoff，原 R87 商系数
包络仍给约 \(10^{12}\) 的相应粗预算；这不是实际反射的下界。

R85 严格给完整物理 contact 上界 \(800K_{\rm trial}(N)\)，包含
regular \(\lambda\) 输出。contact-to-wave 的 root 角、height、
shear 常数须另外付，R92 canonical/physical 列尾也未由本篇替代。
这些数目前不能支持可算的反馈低块，因此不登记为高频逆闭合。

下一项实际改进的对象是扩大真实正侧覆盖以移动 cutoff，以及用根
Taylor 和完整有限余项收紧 \(D_B/s^2,E/s^k\) 等商。R89/R90 的
物理压缩能量只能在保持完整 Schur 耦合后使用；不能直接拿限制
contact 代替这里的完整 contact。

重放：

```bash
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python -u scripts/fourfold_phase_airy_factorized_source_budget.py \
  --out notes/2026-11-12-actual-factorized-airy-source-budget.json
```
