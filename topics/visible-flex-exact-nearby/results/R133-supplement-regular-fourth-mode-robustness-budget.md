# R133：实际外端口容许第四 regular 线的非零指数费用

**已证明（同一实际中心的鲁棒端口预算）。** 本篇回答真实外尾联立中的
一个具体限制：$m=4$ 的允许线不必准确等于 $-4\omega$；若它与全部其余
模一样落在明确指数小盒内，已验证的最终 moving 候选仍可接到真实
periodic-long 输入图。这里不宣称产生该允许线的新尾构造已经完成，
也不删除远端 nonlinear 标签方程。

## 1. 完整假设和一个统一有理费用

保持同一个实际 $a_R,\omega,B$、反射类、原 periodic-long 段和独立
$f_B$。假定新真实允许线对所有 $m\in4\mathbb N$，**包括 $m=4$**，
满足

$$
 |\lambda_m+m\omega|<2^{41}m\omega e^{-2mL},
 \qquad L=\omega(2^{24}-25/8),\quad \omega>7/5.           \tag{Q.1}
$$

仍取真曲率乘子
$q_m=-\lambda_m/[m\omega\sqrt{1+w_R^2}]$。
于是以 $q_*=(1+w_R^2)^{-1/2}$ 及 $\varepsilon=2^{-512}$，有

$$
 |q_m-q_*|<2^{42}e^{-8L}<\varepsilon.                    \tag{Q.2}
$$

因为 $L>(7/5)(2^{24}-25/8)>2^{24}$，且 $e>2$，
$8L>555$，所以

$$
 (2^{42}+8)e^{-8L}<2^{43-8L}<2^{-512},\qquad
 2e^{-6L}<2^{1-6L}<2^{-512}.                            \tag{Q.3}
$$

这些是严格解析比较，不把小指数当成数值下溢后的零。
原目标给 $0.99999999999936<q_*<0.99999999999937$，
因此扩大的全部真实 $q_m$ 仍严格在 $(0,1)$。
原 dyadic proposal 到 $q_*$ 的完整参数误差小于
$9.15\,10^{-18}$，加 (Q.2) 后仍小于 $10^{-17}$。

## 2. 同一实际候选与完整物理行

[最终中心完整端口证书](R133-supplement-final-moving-centre-actual-regular-boundary.md)
的准确候选 SHA 为
`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`。
其全部物理频率与 mean 已给

$$
 Z=(C-C_{\rm ref})_\perp,\quad
 \|Z\|_{A_0}<2.532986\,10^{-13},\quad
 \|b+q^{\rm old}Z\|_{A_0}<1.256750\,10^{-15},
$$
$$
 |C_0-C_{\rm ref}|<6.055\,10^{-43},\qquad B_0=0.          \tag{Q.4}
$$

原已证允许线也满足 $|q_m^{\rm old}-q_*|<\varepsilon$，
第四模为零费只是更强的特例。故新旧**完整**乘子差满足

$$
 \|b+q^{\rm new}Z\|_{A_0}
 <1.256750\,10^{-15}+2\varepsilon\|Z\|_{A_0}.            \tag{Q.5}
$$

这一步直接比较两条完整真实线，不需要重解有限边界，也没有把旧第四
exact-zero 标记转授给新对象。它同时覆盖所有未保留物理模。

## 3. 真长段非线性和两个 mean

固定已实际进入的较小输入球
$r_Z=10^{-12}$，保独立 $r_B=2^{-60}$。令

$$
 r_f=10(r_Z+r_B),\quad F=r_f+r_B,\quad H=6F.
$$

原完整 $C\to f_*$ 图不依赖第四线严格准确性；其真实像与 Lipschitz 界为

$$
 {\rm image}\le9r_Z+\varepsilon r_B+9\,2^{12}F^2<r_f,
 \qquad {\rm Lip}\le36\,2^{12}F<1.                       \tag{Q.6}
$$

$2F<2^{-25}$、$H<2^{-20}$ 也成立。只把真 regular–finite-long 差的
完整统一费更新为 (Q.3)，就得到

$$
 \|d_{\rm new}(Z,f_B)\|_{A_0}
 \le\varepsilon r_Z+\varepsilon r_B+2^{14}F^2
 <1.638404\,10^{-18},
$$
$$
 |c_0(Z,f_B)|\le2^{11}F^2,\qquad B_0^{\rm long}=0.
 \tag{Q.7}
$$

与 (Q.4)–(Q.5) 相加，实际同中心的全部非线性边界行满足

$$
 \boxed{\|b+q^{\rm new}Z-d_{\rm new}(Z,f_B)\|_{A_0}
                        <1.258389\,10^{-15},}
$$
$$
 \boxed{|C_0-C_{\rm ref}-c_0(Z,f_B)|<2.048004\,10^{-19},
 \qquad B_0-B_0^{\rm long}=0.}                          \tag{Q.8}
$$

完整 $C\to f_*$ 导数仍小于10；非均值余项导数小于
$6\,10^{-6}$，mean 余项导数小于 $8\,10^{-7}$。
规范化主体边界行仍要除以准确 $\alpha$。

## 4. 真正执行的有理计算与范围

[有理程序](../scripts/fourfold_regular_fourth_mode_robustness.mjs)在
functions 的 JavaScript 运行时已实际执行：全部分数采用 BigInt
整数的加、减、乘、除、约分和严格交叉相乘比较，没有浮点比较。
19个严格门全部通过；结果是
[完整文本报告](../notes/2026-11-13-R133-regular-fourth-mode-robustness-rational.json)。

它使用 (Q.4) 的已证明有理上界，不重建或伪造旧二进制 native，
也不为原 native 发明文件哈希。复现不依赖 Python/Arb：

```sh
node scripts/fourfold_regular_fourth_mode_robustness.mjs \
  > notes/2026-11-13-R133-regular-fourth-mode-robustness-rational.json
```

独立 mean 高度常数、$f_B$ 和
$k_B(a)+C_Lf_B(a)-S_Lf_*-E_D(f_B(a),f_*)=0$ 继续保留。
新的固定 connector/平台参数方案若能实际证明 (Q.1)，便可消费本篇；
本篇没有替它证明新尾存在或全频标签逆，也未闭合主体全 BVP。
