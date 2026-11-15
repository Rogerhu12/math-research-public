# Benois–Büyükboduk 的 CM–PR 引用在原高权分支上的适用范围

日期：2026-11-15。状态：**已完成引用范围核查；未取得本题原高权特殊化非零输入。**

本注只记录可亲读原文所支付的范围，不判断 Benois–Büyükboduk 的结论是否有其他证明，也不将其视为错误。后续若取得刊本的补充论证或另一完整定理，应重新检查其对本题三个固定角色的适用性。

## 1. 需要支付的实际量

保留 R804、R806、R814、R818 和 R826 的完整角色、所选普通地点及周期。三个原角色为

$$
\lambda_j=\eta_j^{-1}\psi_0^3,\qquad j=4,10,16.
$$

其模形式权为 \(4\)，中心为 \(2\)，且 R818 已证明三个复中心导数非零。对应 norm-weight-one 角色及其共轭为

$$
\nu_j=\eta_j\psi_0^{-1}\bar\psi_0^2,\qquad
\nu_j^*=\lambda_j\mathsf N^{-1}.
$$

因而 \(\nu_j\) 型为 \((-1,2)\)，\(\nu_j^*\) 型为 \((2,-1)\)。本题仍需的是原 canonical 类的指定局部化，等价于 R804 的 \(I_{j,-2}\ne0\)，而不是一个任意 Iwasawa 类非零或复 \(L'(\lambda_j,2)\ne0\)。

## 2. BB 的实际陈述与本次核验版本

亲读版本是 Benois–Büyükboduk，*Arithmetic of critical \(p\)-adic \(L\)-functions*，arXiv:2403.16076v1（2024-03-24）。其 §3.2.5.2–3.2.5.3 先固定中央特殊化 \(c\)，并定义

$$
(\mathrm{PR})\qquad \operatorname{res}_p(c)\ne0.
$$

Remark 3.18(iii) 声称在 CM、解析秩至多一时可以得到 (PR)，所列依据为 [BDP12] 及 Kato [Kat04, §15]。§5.3.2 再依赖该 remark，在 CM 情形删除 (PR) 假设。该 arXiv 版本的参考文献明确将 [BDP12] 定为下节所列 Pacific Journal 论文。

作品已经列为 *Memoirs of the AMS* **321** (2026), no. **1635**，DOI **10.1090/memo/1635**。本次未取得可逐式读取的刊本全文；两位作者网页所给可读稿仍为上述 arXiv 版本。本注因此**不声称已核验刊本是否改写或补充 Remark 3.18**。

## 3. BDP12 真正支付的无穷型

BDP12 为 Bertolini–Darmon–Prasanna，*p-adic Rankin L-series and rational points on CM elliptic curves*，*Pacific J. Math.* **260** (2012), 261–303。

有三个直接、彼此相容的范围标记：

1. Introduction 的 Theorem 2（刊页 265，作者 PDF 第 6 页）处理的 \(\nu\) 明确为**型 \((1,0)\)**；其结论是 CM 阿贝尔簇的点对数。
2. Theorem 3.12（刊页 283，PDF 第 24 页）的证明明确从所引广义公式取 **\(k=2,\ r=j=0\)**，随后用 Abel–Jacobi 与形式群对数的身份。
3. Remark 6（刊页 266，PDF 第 7 页）把型 \((1+j,-j)\) 的进一步讨论指向后续工作。该 remark 并未在本论文中给出 \(j>0\) 的指定局部 Abel–Jacobi 非零定理。

§3D 确有一般权的 Rankin–Katz 分解；这不将上述点对数非零定理自动扩为任意高权特殊化非零。特别是本题型 \((2,-1)\) 对应 \(j=1\)，不能直接以 Theorem 2 或 Theorem 3.12 的点对数结论处理。

## 4. Kato–LLZ 比较所增加及未增加的内容

Lei–Loeffler–Zerbes，*Critical slope p-adic L-functions of CM modular forms*，Theorem 2.28，明确将 Kato [Kat04, (15.16.1)] 写成同一规范的 Euler 系统身份

$$
\Phi_{\psi,f}
\bigl(e_\infty(\gamma)\otimes(\zeta_{p^n})^{\otimes(-1)}\bigr)
=z_{\gamma'}^{\mathrm{Kato}}.
$$

其前置映射引用 Kato (15.12.1)，并保留 Betti／de Rham 比较和实际复共轭分量。这个身份可用于原椭圆单位与 Kato 来源的相认；R826 附录 B 已按原角色使用相应的 critical-slope 公式。

但一个 Iwasawa 元素的身份，或其作为整族不恒为零，并不单独排除某个指定中央特殊化为零。在本次核验的上述引用链中，**没有找到支付原 \((2,-1)\) 分支指定局部化非零的额外一步**。这不是对 Kato 全文所有可能推论的否定；也不是以局部范围核查取代别的完整证明。

尤其不能将 R826 的实际恒等式

$$
\left.\frac{d}{ds}L_{p,\mathrm{crit},j}
\bigl(\chi_{\mathrm{cyc}}\langle\chi_{\mathrm{cyc}}\rangle^s\bigr)
\right|_{s=0}
=
\Omega^\iota\,34^2c_j\theta^9\Omega_p\,I_{j,-2}^{\,2}
$$

中的右端非零，由形式上已构造左端函数来推出。

## 5. 对本课题的使用规则

本次结论仅为：

> BB 所列的这条引用链，按已亲读的版本和定理范围，尚未支付本题三个原高权 canonical 类的指定局部特殊化非零。

R818 的三个复解析秩一、R817 的单个普通素数检测、R811 的原 canonical 严格核结论及 R826 的精确 critical derivative 身份均原样保留；本注不增加跨 \(p\) 非零、不增加新的中央零，也不把高权类改成椭圆曲线点。

后续真正可用的输入必须逐项补齐：原 \(\eta_j\)、原 \(\lambda_j\)、原普通地点、周期、两个 Euler 因子和指定特殊化。刊本 Remark、一般 Artin 分解或某个邻近权的非零都不能省去这些条件。

## 亲读原文

- [BB，arXiv:2403.16076](https://arxiv.org/pdf/2403.16076)，§3.2.5.2、Remark 3.18、§5.3.2及参考文献 [BDP12]。
- [BB 刊物 DOI](https://doi.org/10.1090/memo/1635)；[Benois 作者页](https://www.math.u-bordeaux.fr/~dbenoua/recherche/)；[Büyükboduk 作者页](https://maths.ucd.ie/~kazim_b/research.html)。刊本内容的核验边界见 §2。
- [BDP12 作者 PDF](https://www.math.mcgill.ca/darmon/pub/Articles/Research/52.BDP2/bdp-pjm.pdf)，Theorem 2、Remark 6、Theorem 3.12、§3D。
- [LLZ 原稿](https://arxiv.org/pdf/1112.5579)，Theorem 2.28 及其对 Kato (15.16.1) 的明确引用；刊本 *Israel J. Math.* **198** (2013), 261–282。
- [Kato 原始文献](https://www.numdam.org/item/AST_2004__295__117_0/)，*Astérisque* **295** (2004), §15。此链接用于定位原引用；本注未声称取得一个超出上文已核比较式的高权特殊化非零定理。
