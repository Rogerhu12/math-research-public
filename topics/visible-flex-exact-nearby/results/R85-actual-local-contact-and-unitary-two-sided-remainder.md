# R85：真实局部完整 contact 与酉反射的双侧二阶余项

2026-11-12，independent-audit。

**状态：完整证明并实际支付局部完整源常数；完整 Airy 残差常数仍待接齐。**
本篇将当前整帽对根领口源的完整 contact 常数降到严格小于 800。
解仍在 R69/R74 的整个真实外区上，regular 平均通量行与 root 零模均保留。
另证明在同一完整 balanced flux Hilbert 空间中，只需付反射误差的右二阶
增益，就可由真正酉性得到左二阶增益，免去 R81 的巨大高阶反射范数。

## 1. 当前公共盒、真实整帽和局部空间

参数取已登记公共盒
\[
 \delta_5=-7789843107295549/4611686018427387904,
 \qquad |\delta-\delta_5|\le1/2500000.
 \tag{85.1}
\]
它严格在 R66/R69/R74 实际正外区的 \(\delta_4\pm5\,10^{-7}\) 盒内。
使用根锚定物理角 shear 坐标 \((x,\varphi)\)，\(x=r-t(\delta)\)。令
\[
 L=25/8-t(\delta),\qquad l=1/4-t(\delta).
\]
完整正 form 是 R74 同一个
\[
 b(u,v)=\int_0^L C\nabla_xu\cdot\overline{\nabla_xv}
              +\langle\Gamma_Hu(L),v(L)\rangle,
 \qquad \nabla_x=(\partial_x,\sqrt{x}\partial_\varphi).
 \tag{85.2}
\]
真实 \(\Gamma_H\ge0\) 包含完整无限尾和正确的角密度拉回，
\(\Gamma_H1=0\)。它在常数上的此定义只为 form；真正 regular 平均值
和平均通量条件仍是两个有限槽。

转折 trace 与 regular 物理平均为
\[
 X=H^{1/3}(S^1)\oplus\mathbb C,\qquad
 h=(a,\xi),\quad u(0)=a,\quad
 \langle J u(L),\phi_0\rangle=\xi,
 \tag{85.3}
\]
\(\phi_0=(2\pi)^{-1/2}\)。完整 contact 空间是
\(X^*=H^{-1/3}\oplus\mathbb C\)，第二槽是实际 \(\lambda\)，不是被
商掉的任意常数。R74 已给同一全域问题的唯一强解。

根领口 \([0,l]\) 上实际有 \(m_c I\le C\le M_cI\)，整个正域有
\(C\le M_gI\)。由已完成的同一真实报告，安全数值可取
\[
\begin{gathered}
 .0116031248790358<l<.0116031276614843,\quad L>2.8866031248790358,\\
 m_c>.0247597882015891,\quad M_c<45.3480569344217,
 \qquad M_g<146.9654978965684.
\end{gathered}
\tag{85.4}
\]
程序使用报告中完整有向端点，不使用上面已经放宽的小数。

## 2. 带真实根迹的内部 2/3 估计

对任意 \(u\) 在 \([0,l]\) 上的自然能量空间，成立
\[
 \boxed{\quad
 \|u\|_{L^2_xH^{2/3}}^2
 \le(4+l^2)\int_0^l(|u_x|^2+x|u_\varphi|^2)
       +(4+2l)\|u(0)\|_{H^{1/3}}^2 .\quad}
 \tag{85.5}
\]
这保留实际根迹，因而不需要 R45 无边界条件版本中的 \(l^{-2}\) 质量费。

**证明。** 固定角频率 \(\lambda=|n|>0\)。若
\(h=\lambda^{-2/3}\le l/2\)，R45 的邻区间比较直接给
\[
 \lambda^{4/3}\int|v|^2
 \le2\int|v'|^2+3\int x\lambda^2|v|^2.
\]
否则，由基本定理与 Cauchy--Schwarz，
\[
 \int_0^l|v|^2\le2l|v(0)|^2+l^2\int_0^l|v'|^2.
\]
此时 \(l\lambda^{2/3}<2\)，所以乘以 \(\lambda^{4/3}\) 后不超过
\(4\int|v'|^2+4\lambda^{2/3}|v(0)|^2\)。再对所有频率加上前一个
不带 \(\lambda\) 的质量式，使用
\((1+\lambda^2)^{2/3}\le1+\lambda^{4/3}\)，得到 (85.5)。
\(n=0\) 由同一个质量式直接覆盖。整个证明不假设任一端值为零。

## 3. 真正局部 trace 延拓的纯梯度费

对第 \(n\) 模，令
\[
 (Ea)_n(x)=(1-x/h_n)_+a_n,\qquad
 h_n=\min\{l,|n|^{-2/3}\},\quad h_0=l.
\]
将它在 \([l,L]\) 上延为零。它属于实际 form 空间，根迹为 \(a\)，
regular 平均为零，而且外部 Robin 项准确为零。直接积分给
\[
 \int(|(Ea)_n'|^2+x n^2|(Ea)_n|^2)
 =\left(h_n^{-1}+\frac{n^2h_n^2}{12}\right)|a_n|^2.
\]
因此
\[
 \boxed{\quad
 E_\nabla:=\max\{l^{-1},13/12\},\qquad
 b(Ea,Ea)\le M_c E_\nabla\|a\|_{H^{1/3}}^2 .\quad}
 \tag{85.6}
\]
高频 \(h_n=|n|^{-2/3}\) 时括号等于
\((13/12)|n|^{2/3}\)。低频设 \(s=n^2\in[0,l^{-3}]\)，比值
\[
 f(s)=\frac{l^{-1}+l^2s/12}{(1+s)^{1/3}}
\]
的导数符号是一个递增的仿射式，故其最大值在两端；端值分别为
\(l^{-1}\) 与 \((13/12)(1+l^3)^{-1/3}\)。这证明完整的常数 13/12。
分段线性径向帽只用于 H¹ form 延拓，不要求它是 C² 几何扰动。

## 4. 正能量最小化支付同一整帽的局部 Poisson

记实际齐次 Poisson 解为 \(H(a,\xi)\)。若 \(\xi=0\)，它与 (85.6)
的延拓有相同全部 trace 条件。由实际调和性和 form 非负，
\[
 b(H(a,0),H(a,0))\le b(Ea,Ea).
 \tag{85.7}
\]
这用的是整个非径向正域的同一个解，绝不在 \(x=l\) 人工增加边界条件。
把 (85.7) 和局部 \(C\ge m_cI\) 代入 (85.5)，得到
\[
 \|H(a,0)\|_{L^2(0,l;H^{2/3})}\le C_a\|a\|_{H^{1/3}},
\quad C_a^2=\frac{(4+l^2)M_cE_\nabla}{m_c}+4+2l.
 \tag{85.8}
\]

regular 平均列也必须保留。取真实延拓
\(e(x,\varphi)=(x/L)\phi_0\)。实际角图度数为一，故
\(\langle J\phi_0,\phi_0\rangle=1\)；于是它的 regular 平均值准确为 1。
又因 \(\Gamma_H\phi_0=0\)，
\[
 b(e,e)\le M_g/L.
\]
同一最小化与 (85.5) 给
\[
 \|H(0,\xi)\|_{L^2(0,l;H^{2/3})}\le C_\xi|\xi|,
 \qquad C_\xi^2=\frac{(4+l^2)M_g}{m_cL}.
 \tag{85.9}
\]
线性、三角不等式和二维 Cauchy--Schwarz 因而给
\[
 \boxed{\quad
 \|H:X\to L^2(0,l;H^{2/3})\|
 \le C_{\rm loc}:=\sqrt{C_a^2+C_\xi^2}.\quad}
 \tag{85.10}
\]

## 5. 完整普通源/contact：实际常数小于 800

R45 的准确 \(K=-H^*\) 在同一个实际 realization 中成立。对支撑于
\([0,l]\) 的完整普通源，由 (85.10) 的对偶，
\[
 \boxed{\quad
 \|Kf\|_{H^{-1/3}\oplus\mathbb C}
 \le C_{\rm loc}\|f\|_{L^2_xH^{-2/3}},\qquad C_{\rm loc}<800.
 \quad}
 \tag{85.11}
\]
其中 regular \(\lambda\) 输出、root 零模、两者与其它角模的 cross
都包括在该 Hilbert norm 中。此式不是只估 root 的一个投影。

源 `scripts/fourfold_phase_local_contact_budget.py` 以 256-bit Arb 读取
实际已完成报告并验证完整对象、参数包含及尾的接合关系，得到

| 实际量 | 向外放宽的安全上界 |
|---|---:|
| 纯梯度 trace 延拓平方费 \(E_\nabla\) | 86.183680 |
| root 列局部 Poisson \(C_a\) | 794.615595 |
| regular 平均列局部 Poisson \(C_\xi\) | 90.693884 |
| 完整局部 Poisson/contact \(C_{\rm loc}\) | **799.774545** |

如果 root 输入只有 \(|n|\ge (2/l_-)^{3/2}\) 的物理 shear 角模，
(85.6) 可用 13/12，得到 \(C_a<89.111609\)。这项高频常数只针对该
准确物理 Fourier 投影；不能未经真实角图费用直接将它转授给 canonical
Fourier 投影。完整 (85.11) 不需要这个高频限制。

一般体源仍分解为 \(f=f_{\rm collar}+f_{\rm rest}\)，使用
\[
 \|Kf\|\le C_{\rm loc}\|f_{\rm collar}\|_{L^2H^{-2/3}}
                 +C_{\rm full}\|f_{\rm rest}\|_{L^2H^{-2/3}}.
 \tag{85.12}
\]
\(C_{\rm full}\) 和 regular 非齐次负荷继续由 R81 的同一完整实现支付。
没有把局部试解源的改进错误转授给整个外部普通源。

## 6. 整个增广通量空间中的真实 onto unitary

先在 grounded 物理 root 角中令
\[
 \mathcal H=L^2(S^1)\oplus\mathbb C,\qquad
 Q=\operatorname{diag}(\langle D\rangle^{1/3},1).
\]
完整 DN \(\Lambda:X\to X^*\) 满足
\(\langle\Lambda h,h\rangle=b(Hh,Hh)\ge0\)，并由 Green 恒等式为
自伴。因此 \(T=Q^{-1}\Lambda Q^{-1}\) 是 \(\mathcal H\) 上有界自伴
算子，包含 root 零模和 regular 有限端口。

按一个固定 Green 符号取
\(z_+=(x-iy)/\sqrt2,z_-=(x+iy)/\sqrt2\)，其中
\(x=Qh,y=Q^{-1}(p,\lambda)\)。真实边界图的反射为
\[
 R_B=(I+iT)(I-iT)^{-1}.
 \tag{85.13}
\]
\(I\pm iT\) 都 onto，逆 norm 至多 1；故 \(R_B\) 是准确的 onto
unitary。这也适用于加上任意已付有界实自伴 root shear 后的 \(T\)，
无需该 shear 很小或保持正性。

R83 的真实角换元、正 height 与 \(L_1/2\) 实 shear 保持同一 Green
配对，不能只保主半密度。接入 R39 的完整 Airy frame 时，采用它的
准确通量因子 \(c_J=\pi c_A/2\)，并在 regular 有限端口也使用同一个
因子；例如将上面 \(z_\pm\) 同乘 \(\sqrt{c_J}\)。这样 R39(3.10)
的 \(J=\operatorname{diag}(I,-I)\) 与整个增广空间准确一致。
R53 共根剪切
\[
 \mathscr S_0=\begin{pmatrix}I&\Gamma^{-1}M_{v_0}\Gamma^{-1}\\0&I\end{pmatrix}
 \tag{85.14}
\]
在 root Cauchy 槽作用，在 regular 有限槽作用为恒等。\(\Gamma\) 在
root 零模上按 R53 取 1；实 \(v_0\) 保证 shear 自伴。没有把它限制在
非零模后丢掉零模耦合。

下面的简短 Hilbert 空间论证给这些有界可逆 Green 变换后的 onto
性，不需要额外 Fredholm 或高 Sobolev 假设。一个 unitary 图
\(S=\{(a,Ra):a\in\mathcal H\}\) 满足 \(S=S^{[\perp]}\)，其中
\([\cdot,\cdot]\) 为 \(J\) 配对。任意有界可逆 \(J\)-unitary 变换
保持该恒等式。新图为中性空间，所以正、负投影的范数相等；变换逆的
下界保证两个投影的范围闭。若正投影范围的正交补含 \(y\)，则
\((y,0)\in S^{[\perp]}=S\)，中性又迫使 \(y=0\)。故正投影 onto；
负投影同理。新图因此仍是完整 \(\mathcal H\) 上的 onto unitary 图。

这证明本节后面使用的 \(R\) 确实处在同一个完整 common-root Airy
flux Hilbert 空间，而不是在另一个 frame 中或删均值后借用酉性。
regular \(\lambda\) 与实际尾的有限兼容方程仍须在全反馈中施加。

## 7. 右二阶增益直接给左二阶增益

令 \(R\) 为上节同一真实 unitary，\(S=R+I\)。在完整增广空间中取
\(\mathcal L=\operatorname{diag}(\langle D_\phi\rangle,1)\)，其中
\(D_\phi\) 是实际 canonical 圆长的物理频率。若
\[
 \|S\mathcal L^2\|_{\mathcal H\to\mathcal H}\le C_2,
 \tag{85.15}
\]
则取伴随给 \(\|\mathcal L^2S^*\|\le C_2\)。准确代数
\[
 S=S^*R
 \tag{85.16}
\]
立即给
\[
 \boxed{\quad \|\mathcal L^2S\|\le C_2.\quad}
 \tag{85.17}
\]
闭算子意义下，先在有限 Fourier 数据上验证，再由有界延拓和
\(\mathcal L^2\) 的闭性得到全域结论。Hilbert 尺度插值还给
\(S:H^s\to H^{s+2}\)、\(-2\le s\le0\)，norm 不超过同一个 \(C_2\)。
证明完全不使用 \(\|R\|_{H^2}\)。

对 signed 角权 \(W_\sigma\) 的相同机制是
\[
 S_\sigma=S_{-\sigma}^*R_\sigma.
 \tag{85.18}
\]
因此只要在**同一个实际 frame** 已付两符号的右增益
\(\|S_{-\sigma}\mathcal L^2\|\le C_{-\sigma}\) 与
\(\|R_\sigma\|_{\mathcal H}\le B_\sigma\)，便有
\(\|\mathcal L^2S_\sigma\|\le C_{-\sigma}B_\sigma\)。普通 L² 酉性
不等于非零权下自伴；本篇未把尚需转换到 canonical frame 的加权常数
默认为 1。

## 8. R53 完整试解、有限槽和真正所需的 source 窗口

令真实 Poisson 解产生的 trial incoming/outgoing 为
\(A_{\rm in}=I+E_A\)、\(A_{\rm out}=-I+E_B\)。同一个完整边界图满足
\(RA_{\rm in}=A_{\rm out}\)，所以
\[
 S=E_B-RE_A,
 \qquad
 \|S\mathcal L^2\|\le
 \|E_B\mathcal L^2\|+\|E_A\mathcal L^2\|.
 \tag{85.19}
\]
这里使用的仅是上节已明确的 \(\|R\|_{L^2}=1\)。

有限输入 \(P_f\mathcal H\) 可以包括 root 零模及 regular 平均端口。
在这些输入上取零 trial，则
\[
 A_{\rm in}P_f=A_{\rm out}P_f=0,
 \qquad E_AP_f=-P_f,\quad E_BP_f=P_f.
 \tag{85.20}
\]
这些列照样进入 (85.19)，费用至多 1 加 1，真实反射并未在这些列
上设成 \(-I\)。regular 通量输出对其它 trial 列则由 (85.11) 的
完整 contact 估计保留。因而既没有删均值，也没有暗中把有限低块反演。

对非零 root 输入，R53 corrected Ai trial 的真实物理源具有
\(H^s\to L^2H^{s+5/3}\) 的增益。取 \(s=-2\)，它落在
\(L^2H^{-1/3}\subset L^2H^{-2/3}\)，所以只需 (85.11) 的基础
contact 窗口。经过真实 root 动量归一化的 \(1/3\) 增益，得到
\(E_A\mathcal L^2,E_B\mathcal L^2\) 的 L² 界。R47 的全 Fourier lag
规则在此 source 档只要求整数
\(p>|-2+5/3|+1=4/3\)，可取 \(p=2\)，而非先付四阶或更高 cap
contact。

确切地，若已在 (85.2) 的真实坐标中付
\[
 \|f_{\rm trial}\mathcal L^2:
 \mathcal H\to L^2(0,l;H^{-2/3})\|\le K_{\rm trial},
 \tag{85.21}
\]
且实际根 trace 比较费为 \(T_A,T_B\)、contact-to-wave 两个槽费用
为 \(N_A,N_B\)，那么非零 trial 列可取
\[
 K_A=T_A+800N_AK_{\rm trial},\qquad
 K_B=T_B+800N_BK_{\rm trial}.
 \tag{85.22}
\]
再保留 (85.20) 的有限费用，(85.17) 给真实左二阶余项。
所有 \(N_\pm\) 都必须使用 R83 的实际角、高度和实 shear；物理体源
换元也必须计入 \(K_{\rm trial}\)。本式没有从根值界推断整个 collar
的源界。

若后续使用第 \(j\) 个四重模，实际
\(\lambda_j=4q|j|\)、\(q=2\pi/\ell\)。从本篇物理二阶 norm 转入
R34 的归一整数 cutoff 时，必须保留这个 \(16q^2\) 因子及两个有限槽。
有限低块仍是同一个全反馈低块，不因为右左增益互换而消失。

## 9. 实际记录与下一常数

实际报告为 `notes/2026-11-12-actual-localized-full-contact.json`，包含
所有准确输入 SHA、公共参数盒、完整空间约定和有向常数。重放为

```bash
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_local_contact_budget.py \
  --out notes/2026-11-12-actual-localized-full-contact.json
```

本篇已实付 800 这个完整局部算子常数，并排除了主 cutoff 对
\(10^{60}\) 级高阶 contact 费的结构性依赖。它尚未给出完整
\(K_{\rm trial}\)、\(N_\pm\) 的实际最终值：R83 的根系数之后，仍须付
真实 canonical 正 collar 的有限延拓余项、实际 cutoff 与完整源换元。
接齐后才可给总余项、最终高频 cutoff 和可计算的同一有限低块。
R81 的高阶窗口保留作后续 tame 正则，不再用它不必要地放大本篇的
L² 主频余项。
