# R900 — 原端点在惰性辅助层的根数奇偶、单素层全返回与双新分量

日期：2026-11-16。**状态：已证明。** 本篇继续 R897 的同一原 q/q⁴ 端点，不更换循环、CM 符号或 tame test vectors。对一个良好惰性辅助素数 ℓ，原始有界反循环类的全部非平凡 ℓ-ring-class 分量都为零；整个类准确是首层 restriction 的一个已知标量倍。因此可以在这个单素层真正、有界地除掉 ℓ+1。对两个惰性素数，尚有同时在两素处分歧的原分量，下面给出其完整直和位置和两条迹零式，并不把单素层的整除结论外推到该分量。

这些结论不要求原端点首层非零。它们没有证明 R893 的增广阶 s=0，也没有把原端点与 canonical 椭圆单位系统相认。

## 1. 原来源及两套角色约定

固定 R897 的普通 p>211，以及一个原最高角色 i∈{4,10,16}。仍取
$$
K=\mathbf Q(\omega),\qquad \delta=1+2\omega,\qquad
\lambda_i=\eta_i^{-1}\psi_0^3,\qquad
\phi_i=\lambda_i\mathbf N^{-2}.
\tag{1}
$$
原有限 η_i、2、3、17 处的全部分量按 R806/R814 保留。特别地
$$
\mathfrak f_{\lambda_i}=(34\delta),\qquad
\varepsilon_{\lambda_i}=\eta_K,\qquad w(\phi_i)=-1.
\tag{2}
$$

在 Castella [Ca] 的几何互反约定中，λ_i 的 infinity type 为 (-3,0)，φ_i 为 (-1,2)。R811(8) 已付的真实表示对应为
$$
V_i=T_{\phi_i^\tau}\otimes E,
\qquad
\operatorname{HT}_{(\mathfrak p,\bar{\mathfrak p})}(V_i)=(2,-1).
\tag{3}
$$
所以原 highest balanced 条件是 𝔭 处全、bar𝔭 处零，恰为这个表示的 Bloch–Kato 条件。T_{φ_i} 的条件则相反。下文需要的是 compact Bloch–Kato Selmer 群，绝不以 [Ca] 另一方向的 v-Selmer 群替代。

令 K∞/K 为原反循环 Z_p 扩张，Λ=O[[Γ]]。记
$$
\mathfrak D_i=\widetilde{\mathbf D}_{i,1}
$$
为 R885/R897 的原有界 wild 类。其增广为
$$
\operatorname{sp}_0\mathfrak D_i=\mathscr E_p\,c_{i,1},
\tag{4}
$$
其中 c_{i,1} 是原端点 AJ，𝓔_p 是 R885 的完整普通 Euler 单位，不约定成1。

这里的波浪号始终表示 ACR(6.5) 的原始类，经原固定对应和最高角色提取后所得；不是 R897(A7) 的 split-prime divisor-sum 修正，也不是 R886 的三额外 Euler 单位归一。

## 2. 惰性层仍是同一原始几何来源

设 n 为平方自由整数，其素因子均在 K 中惰性，且与 30·34p 互素。令 K[n]/K 为导子 n 环类域的最大 p 子扩张。

ACR(6.5) 的原始类是对**每个**平方自由 n、(n,Np)=1 定义的；只有随后 Theorem 6.5 的四因子 Euler 修正限制到分裂素数集合。因此此处直接使用(6.5)，不把该 theorem 的允许集合自行扩大。

原三形式仍为 R897(2) 的三个 weight2 CM 形式，原向量仍为
$$
f(Q),\quad g(Q),\quad 4h(Q^4).
\tag{5}
$$
n=1 的比较、X₀/X₁ 次数、旧副本 6⁻²、12⁻² 和第三槽4，全沿 R897 §2–3 固定一次。排除 ℓ=5 后，同一辅助 θ₅/C₅ 仍可用于各层，且 C₅=-216。这里没有引入 R804 的30平滑。

原 first-slot CM 商、Shapiro、ordinary 投影及退化映射对这些 n 仍全数定义；ACR §6.2、(6.3)–(6.5) 没有使用 ℓ 分裂。R897 的同格有界性证明也原样适用这些原始类：几何 Gysin、固定 test-vector 对应和整 CM 商只有一次固定清分母。故有共同稳定格 𝒯_i=p⁻ᶜT_i，使
$$
\widetilde{\mathbf D}_{i,n}\in
H^1_{\rm Iw}(K[n]_\infty,\mathcal T_i)
\tag{6}
$$
对这些 n 全部成立。

### 2.1 原始惰性类的局部条件

ACR Proposition 6.6 的陈述使用其修正后 split 系统，但其局部证明先作用于同一原始几何类，且不要求新增 tame 素数分裂：

- 在 p 处，BSV Corollary 8.2 的 balanced 局部性适用于原 ordinary 对角来源；新增 n 的退化映射为 p 处良好 tame 对应，与 ordinary filtration 相容。ACR(6.3) 的固定三个提取映射和(6.4)的 CM/Shapiro 同构保持这些局部子空间。
- 在 v∤p 处，ACR Proposition 4.9 / Proposition 6.6 的纯权−1及局部对偶论证给有理 H¹=0。这包括 v|n。其整局部群仅有挠，正是传播的 Greenberg 条件。
- 最高 CM 提取后，p 处两子空间恰为(3)的全/零条件。有限 n 角色在 p 处不分歧，不改变这两个 Hodge–Tate 指数。

因此(6)属于原 compact balanced=BK Selmer 群。此处没有从范数式反推局部条件。

## 3. 原完整 wild 范数的准确标量

对 ℓ∤n 良好惰性，由三个形式均 CM 于 K，
$$
a_\ell(g)=a_\ell(h)=0.
$$
ACR Proposition 6.3(ii) 在 k=l=m=2 的原规范中直接给
$$
\boxed{
\operatorname{cor}_{K[n\ell]_\infty/K[n]_\infty}
 \widetilde{\mathbf D}_{i,n\ell}
=A_\ell\,\widetilde{\mathbf D}_{i,n},
\qquad
A_\ell=-\frac{(\ell+1)^2}{\ell}.
}
\tag{7}
$$
这是完整 Λ 恒等式。没有遗漏 κ_ac(ℓ)、额外 Frobenius 或其增广：该原始公式在惰性情形本身就是(7)的标量。也不能把它直接改称一维 Euler 因子。

为对照，在原算术互反约定下最高表示的角色为
ρ_i=η_i⁻¹ψ₀³/𝑵。由于有理惰性理想 (ℓ) 上
$$
\eta_i((\ell))=1,\quad \psi_0((\ell))=-\ell,\quad
\rho_i(\operatorname{Fr}_{(\ell)})=-\ell,
$$
其真正 one-place 一维 Euler 值为
$$
P_{i,(\ell)}(1)=1+\ell^{-1}.
\tag{8}
$$
(7)与(8)相差 -(\ell+1)。后文用全来源证明何时可以除这个因子。

## 4. 实际环类群及有限角色

置
$$
h_\ell=p^{v_p(\ell+1)},\qquad G_\ell=\operatorname{Gal}(K[\ell]/K).
$$
类数1及 μ₆ 的阶与 p 互素给
$$
G_\ell\simeq
\bigl((\mathcal O_K/\ell)^\times/
             (\mathbf Z/\ell)^\times\mu_6\bigr)_{(p)}
\simeq C_{h_\ell}.
\tag{9}
$$
多素数时同一类域序列和 CRT 给
$$
G_n=\prod_{\ell\mid n}G_\ell.
\tag{10}
$$
对于 ℓ≡-1 mod p，p∤ℓ-1，所以模 (ℓ) 的最大 p-ray 层也等于这个环类层；这里确实只有 K 的一个分歧素点。它与 R897 附录B的 split 两素点局面不同。

设 χ 为 G_n 的角色，按原 Artin 方向作为 Hecke 角色。χ 的阶为 p 幂、χ^τ=χ⁻¹，且在 A_Q× 上平凡。记
$$
S(\chi)=\{\ell\mid n:\chi|_{G_\ell}\ne1\}.
$$
χ 的导子恰为 ∏_{ℓ∈S(χ)}(ℓ)；在每个这样的 ℓ 处为导子指数1的 tame 角色。其局部角色在 F_ℓ× 上平凡，在 uniformizer ℓ 上也为1。

另外，χ((δ))²=χ((-3))=1，而 χ 为奇数阶，故
$$
\chi((\delta))=1.
\tag{11}
$$
这保留了原三处的 additive-character/different 规范。

## 5. 有限域 Gauss 和支付每个根数变化

固定 ℓ∈S(χ)。令 θ 为 χ_ℓ 或其逆在 F_{ℓ²}× 上的非平凡角色；两者下面所得相同。θ 在 F_ℓ× 上平凡，阶为奇数。取任一非零 trace-zero 元素 d，因 d²∈F_ℓ×，有 θ(d)=1。

对非平凡 ψ:F_ℓ→C×，令
$$
G(\theta)=\sum_{x\in\mathbf F_{\ell^2}^\times}
 \theta(x)\psi(\operatorname{Tr}x).
$$
trace-zero 的非零纤维贡献 (ℓ-1)θ(d)=ℓ-1。所有非零 trace 纤维的角色和相同，记为 B；由 Σ_{x≠0}θ(x)=0 得 B=-1。因此
$$
G(\theta)=(\ell-1)-\sum_{a\ne0}\psi(a)=\ell.
\tag{12}
$$
这包括原 trace additive character 的任意 F_ℓ× 单位缩放，因为 θ 对这些单位平凡。

λ_i 在 (ℓ) 未分歧，且 λ_i((ℓ))=-ℓ³。所以其 unitary normalization 在 uniformizer ℓ 的值为−1。局部 tame epsilon 公式与(12)给新增局部比值−1。取 θ 或 θ⁻¹、几何或算术 reciprocity 时该比值都仍为−1。

在其余位，有限 twist 不另贡献根数：

- 2、17 为原惰性坏位，χ 在这两处未分歧且在有理 uniformizer 上取1；
- 3处的所有 conductor/different 因子由(11)取1。等价地，原不同理想与导子的乘积为 (δ)(34δ)=(-102)，其 χ 值为1；
- 其它未分歧有限位的 epsilon 比值为1，∞处 χ 平凡。

由(2)，得到原全部有限角色的精确奇偶式
$$
\boxed{
w(\phi_i\chi)=(-1)^{\,1+\#S(\chi)}.
}
\tag{13}
$$
特别地，单惰性素层的每个非平凡 χ 都使根数变成 +1。这里没有由某个 L 值非零反推符号。

## 6. 用到的已发表 compact BK 消失及方向

本篇使用以下已发表输入的明确高权表述：[Ca, Remark 4.5.2] 对其 self-dual pair 范围给
$$
w(\phi)=+1\quad\Longrightarrow\quad
\check{\mathcal S}_{\rm BK}(\phi)=0.
\tag{14}
$$
这是沿反循环 Z_p 塔、按 corestriction 取逆极限的 compact 群；不是有限层 BK 群消失，也不是反向普通条件的群消失。

把(14)用于 φ_iχ，不需要改动原端点来源。只为核定定理假设，取 R814 已固定的 cyclic ψ（导子仅在所选7、13位），将其有限 good-pair 角色 χ_i^{pair} 换为 χ_i^{pair}χ。此时：

1. ψ 仍为 (-3,0)，所以 r=2；其 cyclic 导子 norm 与 p·3 及 n 互素。
2. λ_iχ 的导子为 (34∏_{ℓ∈S(χ)}ℓ)δ，δ 恰一次，central character 仍 η_K。
3. 这对角色满足 [Ca] S1–S3 / Σ_cc 条件。可直接沿其 Lemma 5.1.2 证明第一段的 cyclic ψ 构造；也可逐位核：新增 ℓ 处两个 CM 因子的 root 各变−1，故 Rankin 有限 epsilon 的乘积仍+1；旧 split 辅助位的 unramified χ 因子相消，原2、3、17位由(11)保持。
4. 不使用 S4；新增 twist 的伴随中心值不被假定非零。p 幂有限 χ 允许系数域分歧；定理没有 p∤|G_n| 这一额外条件。

[Ca] 现已正式发表为 Proc. Lond. Math. Soc. 131 (2025), no.4, e70089，DOI 10.1112/plms.70089。其 Remark 4.5.2 明确引用 Agboola–Howard Theorem 2.4.17 及 Arnold Theorem 3.9 的高权扩展。AH 的原 theorem 在 CM 椭圆曲线、class number one、p>3 良好普通范围；不能仅靠该椭圆版本直接搬到本 weight4。这里直接使用已发表 [Ca] 对上述高权 self-dual pair 的明确陈述；不以尚未取得全文的 Arnold 页面替代假设核对。

还必须真实处理(3)。采用
$$
e_\chi=|G_n|^{-1}\sum_{g\in G_n}\chi(g)^{-1}g
$$
时，Shapiro 将 e_χ 分量识别为 T_{φ_i^τ}⊗χ⁻¹ 的 Iwasawa 上同调。再作 R811 的 τ 共轭，得到 T_{φ_iχ}，并把 Γ 变量作 ι:γ↦γ⁻¹。于是(14)及(13)给
$$
\boxed{
e_\chi\widetilde{\mathbf D}_{i,n}=0
\quad\text{若 }\#S(\chi)\text{ 为奇数}.
}
\tag{15}
$$
τ 同时把 p 的全条件移到 barp 的全条件；固定系数只作标量。因而没有把 φ 与 φ^τ、χ 与 χ⁻¹ 在同一约定下偷换。

角色幂等元仅用于证明有理分量为零，不用于整类的构造。

## 7. 单惰性层的完整类准确是旧 restriction

令 n=ℓ。由(15)，原类在 E[G_ℓ] 中只有平凡分量。因此它被整个 G_ℓ 固定。

这个有理结论可以直接在原格上下降。原十七惯性元素在 𝒯_i/pᴺ𝒯_i 上作用为−1，而 K[ℓ]∞/K 在17处不分歧。故所有相关 H⁰ 为零。有限 G_ℓ 的 inflation–restriction 在每个 wild 层给
$$
H^1(K_m,\mathcal T_i)
 \xrightarrow{\ \sim\ }
H^1(K[\ell]K_m,\mathcal T_i)^{G_\ell}.
\tag{16}
$$
这些同构与 corestriction 相容，取逆极限仍成立。相同 H⁰ 消失还给 O-torsion-free，故有理固定性确实是整固定性。

将(7)与(16)及 cor∘res=h_ℓ 结合，得到
$$
\boxed{
\widetilde{\mathbf D}_{i,\ell}
=-\frac{(\ell+1)^2}{\ell h_\ell}
       \operatorname{res}_{K[\ell]_\infty/K_\infty}
                     \mathfrak D_i.
}
\tag{17}
$$
当 h_ℓ=1 时同式也直接由(7)成立。式中系数的 p 赋值是 v_p(ℓ+1)，因此(17)本身位于原共同格，不增加随 ℓ 增长的分母。

定义
$$
\mathbf e_{i,\ell}
:=-\frac{\widetilde{\mathbf D}_{i,\ell}}{\ell+1}.
$$
(17)真正支付这个除法，且
$$
\boxed{
\mathbf e_{i,\ell}
=\frac{\ell+1}{\ell h_\ell}\operatorname{res}\mathfrak D_i,
\qquad
\frac{\ell+1}{\ell h_\ell}\in\mathbf Z_p^\times,
\qquad
\operatorname{cor}\mathbf e_{i,\ell}
=(1+\ell^{-1})\mathfrak D_i.
}
\tag{18}
$$
这是该同一单素层的 one-place 范数。它的完整来源仍是旧 restriction，并未产生新的 χ 分量。

## 8. 有限端点类与全部 ordinary Euler 的返回

原始类的有限特殊化也使用 R897(A9)–(A12) 的相同 CM 根，惰性 tame 导子不改变 p 处的计算。若 ξ_ℓ=σ_bar𝔭,ℓ⁻¹∈G_ℓ，则
$$
\mathcal E_{p,\ell}=
\frac{(1+\bar\pi^{-1}\xi_\ell)
      (1+\bar\pi^{-1}\xi_\ell^{-1})^2
      (1+\pi\bar\pi^{-2}\xi_\ell^{-1})}
     {(1-\pi\bar\pi^{-1}\xi_\ell^{-2})
      (1-\pi/\bar\pi)^2}
\in\mathcal O[G_\ell]^\times,
\tag{19}
$$
以及
$$
\operatorname{sp}_0\widetilde{\mathbf D}_{i,\ell}
=\mathcal E_{p,\ell}\widetilde c_{i,\ell}.
\tag{20}
$$
(19)在旧 restriction 线上作用为其增广 𝓔_p。由(4)、(17)和(20)，
$$
\boxed{
\widetilde c_{i,\ell}
=-\frac{(\ell+1)^2}{\ell h_\ell}
       \operatorname{res}_{K[\ell]/K}c_{i,1}.
}
\tag{21}
$$
这份**指定原始有限类**的非平凡 χ 分量为零，是由其有界 wild 提升与(14)得到；并未断言这些 χ 的有限 Selmer 群全零。

## 9. 两个惰性素数：唯一未被奇偶消掉的全新块

取不同 ℓ₁、ℓ₂，记 h_r=h_{ℓ_r}、A_r=A_{ℓ_r}。在 G=G_{ℓ₁}×G_{ℓ₂} 上，(15)杀掉“只在一处非平凡”的全部分量。平凡分量由(7)准确确定。因此
$$
\boxed{
\widetilde{\mathbf D}_{i,\ell_1\ell_2}
=\frac{A_1A_2}{h_1h_2}\operatorname{res}\mathfrak D_i
  +\mathbf N_{i;\ell_1,\ell_2}.
}
\tag{22}
$$
余项由这个等式定义于原共同格：A₁A₂/(h₁h₂) 是 p 整数，而原始类和 restriction 均已整。其有理角色支撑恰被限制在 χ₁≠1、χ₂≠1，并满足完整两条
$$
\operatorname{cor}_{K[\ell_1\ell_2]_\infty/K[\ell_1]_\infty}
      \mathbf N_{i;\ell_1,\ell_2}=0,
\qquad
\operatorname{cor}_{K[\ell_1\ell_2]_\infty/K[\ell_2]_\infty}
      \mathbf N_{i;\ell_1,\ell_2}=0.
\tag{23}
$$
这些真实双新角色由(13)恢复 root−1。因而(14)不能再将(22)的余项杀掉。

形式上若想把所有惰性层都归一为一维 Euler 范数，需要除
∏_{ℓ|n}[-(ℓ+1)]。单素层的(18)并不支付双新项
$$
\mathbf N_{i;\ell_1,\ell_2}/((\ell_1+1)(\ell_2+1))
\tag{24}
$$
在同一共同格中整。两条迹零式本身也没有这种整除含义：在原整群环中 (σ₁−1)(σ₂−1) 同时被两个部分范数杀掉，而其显示系数不被 p 整除。这个例子只说明范数代数不能补出所需整除，不声称它就是原几何余项。

更一般地，原 n 层只可能保留在偶数个惰性素数处真正分歧的角色。不同偶数支撑的实际类及其增广阶仍须由原来源继续计算。

## 10. 对原 s 门已经得到、尚未得到的内容

(17)和(21)说明：沿这一原始惰性单素层，有限端点非零、普通局部非零与原首层分别同步。它不会从未知的首层零制造新的非零证据，也不能把一条旧 restriction 的 unit multiple 计为独立来源。

(18)确实实现了一个单素层的整 one-place 返回，但完整辅助素数 Euler 系统还需要(24)及所有更高偶数支撑的有界整除。另在这些惰性素数上，h_ℓ>1 迫 ρ_i(Fr_(ℓ))=-ℓ≡1 mod p，不能将它们当作 R891 的 γ−1 可逆辅助点。

所以本篇关闭的是**同原始来源的全部单惰性层及一般角色奇偶**，并准确留下双新及更高偶数支撑。R893 的 s=0、原 endpoint AJ 非零和无穷 p 主目标均没有由这些恒等式自动推出。

## 原文依据

- Alonso–Castella–Rivero, *The diagonal cycle Euler system for GL₂×GL₂*, DOI [10.1017/S1474748023000221](https://doi.org/10.1017/S1474748023000221)，[作者刊本](https://web.math.ucsb.edu/~castella/ACR1-print.pdf)：§6.2、(6.3)–(6.5)、Proposition 6.3(ii)，刊本 pp35–38；局部条件见 Proposition 4.9、Proposition 6.6 及其 BSV Corollary 8.2 引用。
- Castella, *Tamagawa number conjecture for CM modular forms and Rankin–Selberg convolutions*, Proc. Lond. Math. Soc. 131 (2025), no.4, e70089，DOI [10.1112/plms.70089](https://doi.org/10.1112/plms.70089)；[可检索作者全文](https://arxiv.org/html/2407.11891v3)：Definition 3.4.1、Lemma 3.4.2、Proposition 3.5.1、Remark 4.5.2，及 §5.1 cyclic-pair 假设核对。
- Agboola–Howard, *Anticyclotomic Iwasawa theory of CM elliptic curves*, Ann. Inst. Fourier 56 (2006), 1001–1048，[正式作者 PDF](https://web.math.ucsb.edu/~agboola/papers/bisi_aif_2006.pdf)：Theorem 2.4.17，printed p1034。其原椭圆范围和本篇直接使用的高权 [Ca] 表述已在§6区别。
- Arnold, *Anticyclotomic main conjectures for CM modular forms*, J. Reine Angew. Math. 606 (2007), 41–78，DOI [10.1515/CRELLE.2007.034](https://doi.org/10.1515/CRELLE.2007.034)，是 [Ca, Remark 4.5.2] 明指的高权来源；本文不另据未核的全文范围扩大定理。
