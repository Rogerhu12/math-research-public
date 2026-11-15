# R261：八个新增第三核 hook 的完整四阶自伴局部算子与全十八维核的 Green 表示

日期：2026-11-15。作者责任：当前研究代理完整消费公开 Actions 原日志并整理数学结论，根代理独立读取实际、核对来源与论文。所有新原式运算及八项新增人工检查均在本公开仓库的 Actions 完成；本地仅解析已经发布的日志、转写准确系数及作纸面推论。

## 1. 本次完成的结论

令 $W$ 为原三槽第三空间，$\Delta\tau(q)=\tau(q;q,q)$，$Z=\ker\Delta$。[R254](R254-eight-exact-third-diagonal-lifts-and-eighteen-dimensional-image.md) 已证明

$$
Z=Z_{71}\oplus\operatorname{span}
\{\chi_{30},\chi_{32},\chi_{34},\chi_{37},\chi_{40},
\chi_{100},\chi_{104},\chi_{109}\},\qquad
\dim Z=18,\quad\dim Z_{71}=10.
\tag{1}
$$

本次唯一新目标是八个完整原 hook

$$
K_j(f;w)=\chi_j(w;f,f)
\tag{2}
$$

的真实三阶 profile 导数。八个目标全部得到

$$
D_x^3K_j(f;w)=\mathscr A_{j,f}w,
\qquad
\mathscr A_{j,f}
=D_x^2(a_jD_x^2)+D_x(b_jD_x)+c_j,
\tag{3}
$$

其中 $a_j,b_j,c_j$ 是局部有限 jet 多项式，$\mathscr A_{j,f}$ 形式自伴，并且作为 universal jet 多项式时阶数准确为四（固定 $f$ 可退化），且有

$$
\mathscr A_{j,f}f=0.
\tag{4}
$$

式 (4) 来自 R254 已付的完整对角原身份，没有重跑旧对角目标。本次独立验证的是完整三阶导的局部性、全部系数的自伴性和原式重构身份。

结合 [R258](R258-self-adjoint-hook-green-operator-and-complete-period-interface.md) 的十个旧核方向，(3)–(4) 现对全部 $Z$ 成立。真实共同右零 collar 的三个常数始终保留，故

$$
K_f^\tau(w)=-J^3(\mathscr A_{\tau,f}w),
\qquad
(Jv)(x)=\int_x^{r_*}v(\xi)\,d\xi,
\qquad \tau\in Z.
\tag{5}
$$

这是完整十八维第三对角核的局部自伴表示。它没有声明整个第四 pure 核响应都由这些方向生成，也没有声明固定圆的 period 观测商满射、实际有符号成本可达或 joint ruling 已解。

## 2. 八个目标的原索引与既有完整定义

沿用原 $W$ retained 序列

$$
0,\ldots,27,\ 30,32,34,37,40,100,104,109.
\tag{6}
$$

前 28 个完整交换子记为 $C_i$；原额外模板记为 $\tau_j$。本次消费 R254 已付的完整差

$$
\chi_j=\tau_j-\gamma_j,
\tag{7}
$$

其中

$$
\begin{aligned}
\gamma_{30}&=(3C_2+C_{20})/256,\\
\gamma_{32}&=(C_3-3C_4-C_8)/128-C_{21}/512,\\
\gamma_{34}&=-(C_3+5C_4+3C_8)/128-3C_{21}/512,\\
\gamma_{37}&=(C_5+C_9+2C_{10})/32,\\
\gamma_{40}&=-C_{11}/32,\\
\gamma_{100}&=-C_5/8-C_{10}/4-C_{24}/32,\\
\gamma_{104}&=3C_0/4+C_6/16+3C_{11}/8-3C_{14}/16,\\
\gamma_{109}&=-C_{12}/4.
\end{aligned}
\tag{8}
$$

完整 $\tau_j,\gamma_j,\chi_j$ 的原根 SHA 均逐一匹配 R254。只在匹配后作原三槽代入 $(a;b,c)=(w;f,f)$，继而对含全部右 primitive 的原函数求三次导数。没有先只取局部项、纯幂尾或固定 profile 值。

## 3. 全部八个局部算子的可读系数

本节缩记

$$
p=f',\quad r=f'',\quad t=f''',\quad
u=f^{(4)},\quad v=f^{(5)}.
\tag{9}
$$

这里的 $r,t,u,v$ 只是 profile jets，不是几何状态或端点。记 $d_j$ 为实际完整算子的 $D_x^2$ 系数，并定义

$$
b_j=d_j-a_j'',\qquad
\bar a_j=256a_j,\quad \bar d_j=256d_j,\quad
\bar c_j=256c_j.
\tag{10}
$$

所有撇号都同时微分显式 $x$ 与全部 profile jets。下列三个多项式完整确定五个微分系数：

$$
\mathscr A_{j,f}
=a_jD^4+2a_j'D^3+d_jD^2+(d_j'-a_j''')D+c_j.
\tag{11}
$$

实际分别保留并检查了五个系数；(10)–(11) 是其自伴零差已经通过后的可读重组。以下每个整数系数仅是公开实际有理系数按共同分母 256 改写，没有在本地执行新的导数、消元或正规化。

### 3.1. 原索引 $j=30$

$$
\begin{aligned}
\bar a_{30}&=-3ft-2pr+x(-3pt+r^2),\\
\bar d_{30}&=-3fv-14pu+2rt+x(-3pv-ru+2t^2),\\
\bar c_{30}&=3rv+9tu.
\end{aligned}
$$

### 3.2. 原索引 $j=32$

$$
\begin{aligned}
\bar a_{32}&=4fr+x(6ft)+x^{2}(-3pt+r^2),\\
\bar d_{32}&=18fu+12pt+x(6fv-4rt)+x^{2}(-3pv-ru+2t^2),\\
\bar c_{32}&=-2pv-22ru-20t^2+x(-6rv-18tu).
\end{aligned}
$$

### 3.3. 原索引 $j=34$

$$
\begin{aligned}
\bar a_{34}&=4fr+x(18ft)+x^{2}(-9pt+3r^2),\\
\bar d_{34}&=38fu+28pt+x(18fv-12rt)+x^{2}(-9pv-3ru+6t^2),\\
\bar c_{34}&=2pv-42ru-44t^2+x(-18rv-54tu).
\end{aligned}
$$

### 3.4. 原索引 $j=37$

$$
\begin{aligned}
\bar a_{37}&=x(-8fr)+x^{2}(-36ft+12pr)+x^{3}(24pt-8r^2),\\
\bar d_{37}&=-64ft+x(-136fu+16pt)+x^{2}(-36fv+84pu+24rt)+x^{3}(24pv+8ru-16t^2),\\
\bar c_{37}&=-40pu+80rt+x(-16pv+144ru+160t^2)+x^{2}(36rv+108tu).
\end{aligned}
$$

### 3.5. 原索引 $j=40$

$$
\begin{aligned}
\bar a_{40}&=x^{2}(4fr)+x^{3}(12ft-4pr)+x^{4}(-6pt+2r^2),\\
\bar d_{40}&=x(64ft)+x^{2}(68fu-8pt)+x^{3}(12fv-28pu-8rt)+x^{4}(-6pv-2ru+4t^2),\\
\bar c_{40}&=32pt+x(40pu-80rt)+x^{2}(8pv-72ru-80t^2)+x^{3}(-12rv-36tu).
\end{aligned}
$$

### 3.6. 原索引 $j=100$

$$
\begin{aligned}
\bar a_{100}&=-32fp+x(64fr)+x^{2}(48ft-32pr)+x^{3}(-48pt+16r^2),\\
\bar d_{100}&=256ft+x(288fu-128pt)+x^{2}(48fv-224pu-32rt)+x^{3}(-48pv-16ru+32t^2),\\
\bar c_{100}&=-64pu-320rt+x(-32pv-352ru-320t^2)+x^{2}(-48rv-144tu).
\end{aligned}
$$

### 3.7. 原索引 $j=104$

$$
\begin{aligned}
\bar a_{104}&=96f^2+x(-64fp)+x^{2}(-32fr-32p^2)+x^{3}(-192ft+96pr)+x^{4}(120pt-40r^2),\\
\bar d_{104}&=x(-832ft)+x^{2}(-1024fu+608pt)+x^{3}(-192fv+672pu+128rt)+x^{4}(120pv+40ru-80t^2),\\
\bar c_{104}&=-96fu-768pt+x(-768pu+1088rt)+x^{2}(-160pv+1056ru+1216t^2)+x^{3}(192rv+576tu).
\end{aligned}
$$

### 3.8. 原索引 $j=109$

$$
\begin{aligned}
\bar a_{109}&=x^{2}(-64fp)+x^{3}(64fr+64p^2)+x^{4}(192ft-96pr)+x^{5}(-96pt+32r^2),\\
\bar d_{109}&=x^{2}(1792ft)+x^{3}(1408fu-768pt)+x^{4}(192fv-672pu-128rt)+x^{5}(-96pv-32ru+64t^2),\\
\bar c_{109}&=x(2048pt)+x^{2}(1472pu-2048rt)+x^{3}(192pv-1472ru-1664t^2)+x^{4}(-192rv-576tu).
\end{aligned}
$$

## 4. 原式证据的准确范围

程序将完整原 $D^3K_j$ 映到固定颜色顺序 $(f,w)$ 的原右锚词表示，未删去任何非空词或高阶 $w$-jet。实际八条最终都只剩空词，且外部 $w$-jet 的最高阶为 4，profile 系数最高 jet 为 $f^{(5)}$。局部系数重组后，再由一个独立的新映射器检查完整原差

$$
D^3K_j-\mathscr A_{j,f}w=0.
\tag{12}
$$

| 原索引 | $K_j$ 原项 | $D^3K_j$ 原项 | 完整局部词行 | 重构原差项数 | fresh 原差词数 |
|---:|---:|---:|---:|---:|---:|
| 30 | 16 | 21 | 21 | 0 | 0 |
| 32 | 30 | 28 | 26 | 2 | 0 |
| 34 | 32 | 28 | 26 | 2 | 0 |
| 37 | 51 | 39 | 36 | 3 | 0 |
| 40 | 50 | 45 | 38 | 7 | 0 |
| 100 | 58 | 41 | 38 | 3 | 0 |
| 104 | 81 | 46 | 46 | 0 | 0 |
| 109 | 54 | 44 | 44 | 0 | 0 |

原索引 $32,34,37,40,100$ 的原差分别仍有 $2,2,3,7,3$ 个原 DAG 项，故不能称它们是字面原多项式相同。它们通过的是同右锚分部积分后的完整函数身份。其余三个原差已经字面为零。八条 fresh 原差的完整词表示均为零，无 cycle fallback。

相反，局部算子已经无 primitive；完整形式伴随差

$$
\mathscr A_{j,f}^*-\mathscr A_{j,f}
\tag{13}
$$

在每个目标都是空的原局部多项式。没有仅凭某几个系数或一个对称标签推断自伴。

规范词使用 [R179](R179-universal-independence-of-fixed-color-remainder-words.md) 的固定颜色余字母语法；其原同右锚转换身份保持。本次没有重跑 R179、R254 的十八参考向量、八个旧对角差、旧 151/152 模板或任何旧 fourth 响应。

所有 fresh 零词和局部伴随零差的公共零 SHA 为

`4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`。

## 5. 全十八维核的忠实局部表示

**定理。** 对全部 $\tau\in Z$，存在唯一由 $\tau$ 线性决定的局部自伴算子 $\mathscr A_{\tau,f}$，满足 (3)–(5)，其关于 $w$ 的阶数至多 4；映射

$$
\tau\longmapsto\bigl(f\longmapsto\mathscr A_{\tau,f}\bigr)
\tag{14}
$$

在 universal 函数空间上单射，像的维数准确为 18。

**证明。** R258 已付 $Z_{71}$ 十方向，本次付清 (1) 的另外八方向；线性性给存在性、自伴性及完整右三常数。R254 的 $\Delta\tau=0$ 给 $K_f^\tau(f)=0$，再对原函数求三阶导即得 $\mathscr A_{\tau,f}f=0$。

若 (14) 的像为零，则对所有允许的 $f,w$ 有 $(K_f^\tau(w))'''=0$。由于原 $K,K',K''$ 在共同右 collar 都为零，该二次多项式只能为零。原第三模板内两槽对称，故

$$
2\tau(w;f,g)
=K_{f+g}^\tau(w)-K_f^\tau(w)-K_g^\tau(w)=0.
\tag{15}
$$

所以 $\tau=0$。结合既有 $\dim Z=18$ 得所述像维数；没有重新求一个数值或有理矩阵秩。证毕。

这个 18 是 **随所有允许 $f$ 变化的 universal 局部算子表示** 的维数。它不表示某一个固定 seed $f$ 下的 18 个算子一定独立；常平台或其他特殊 seed 可以发生严格退化。

### 5.1. Green 身份可准确扩展到全 $Z$

本定理的假设足以将 R258、R260 的自伴 Green 公式线性扩展到全部十八方向。若

$$
\mathscr A_{\tau,f}=D^2(aD^2)+D(bD)+c,
\tag{16}
$$

则

$$
\mathfrak B(v,w)
=v(aw'')'-v'aw''-w(av'')'+w'av''
+b(vw'-wv'),
\tag{17}
$$

$$
D\mathfrak B(v,w)=v\mathscr Aw-w\mathscr Av,
\qquad
\Lambda=fK''-\mathfrak B(f,w),
\qquad
\Lambda'=f'K''.
\tag{18}
$$

这些式子从本次已付的新假设推出，不是事后把旧十方向来源直接改称十八方向。对于完整 period，仍须保每个真实活动左端的 $\Lambda(a_j)$，并分别检查平台、总通量、内部 Laurent 与端 germ。

完整两个 mixed 响应也仍保

$$
\begin{aligned}
D&=2K_f^\tau\bigl(\Phi_E(f^2-g^2)\bigr)
 +4\Phi_E(g,K_f^\tau(g)),\\
E&=-4K_f^\tau\bigl(\Phi_E(fg)\bigr)
 +4\Phi_E(f,K_f^\tau(g)).
\end{aligned}
\tag{19}
$$

不能只保 (19) 中第一个 $K$，或从自伴性直接删去 $K_f^\tau(g)$。

### 5.2. 一个可直接读取的常平台后果

在一个真正的常平台 $f=F$ 上，把本稿系数中的 $p,r,t,u,v$ 全置零，只是读取已发局部公式，得到

$$
\mathscr A_{\chi_{104},F}=\frac38F^2D^4,\qquad
\mathscr A_{\chi_j,F}=0\quad(j\ne104).
\tag{20}
$$

这是局部导数算子的陈述。原 $K_f^{\chi_j}$ 在平台上仍由共同右端数据带有准确二次尾；即使 (20) 的局部算子为零，也不授原平台 period 目标为零。

## 6. 公开 Actions、人工检查与真实费用

唯一运行：

- 仓库：`Rogerhu12/math-research-public`。
- run：[43712266529](https://github.com/Rogerhu12/math-research-public/actions/runs/43712266529)。
- job：[132806237299](https://github.com/Rogerhu12/math-research-public/actions/runs/43712266529/job/132806237299)。
- 计算 source：`a934b45c33f7f4807a307b6a556bf32b76db675d`。
- lane：`third_kernel_eight_local_operators`。
- driver：[literature_third_kernel_eight_local_operators.py](../scripts/literature_third_kernel_eight_local_operators.py)，35645 B，SHA-256 `f59143274124c7458571f55313fca00ada93b31ee71d1be2739cbb402bbeb4d3`。
- schema：`visible-flex-third-kernel-eight-local-operators-v1`。
- [metadata-only receipt](../notes/actions-43712266529-1-third_kernel_eight_local_operators/receipt.json)：52008 B，SHA-256 `42c3c1489f0371555d6fba3632e49c4ea44b5b7dfb085499e61f0cba3dbb2598`。

实际开始前完成 terminal pull/read 至 `10de7424185156db208cbbaa0dfaafc547bf5229`，两份 README 均无变化，随后恢复上述已绑定 source 计算。预读小件 253 B，SHA-256 `42be6643a6d6e2fc40b3c212712250ed87b8afc17a683fd7205368a572538974`。本次 request 的 53 项 `source_sha256` 与 receipt 对应项全部一致；consumer 自身的 16 项递归源码身份也逐项相符。

本次先公开运行八项新的人工 adapter 检查：完整局部 $w$-jet 重组、真正内层 $w$ primitive、外 $w$ 乘纯 $f$ 尾、完整四阶伴随、明确非自伴反例、原积分的三导正号、完整同锚 IBP 重构、以及不把六阶目标截成四阶。八项全部通过。没有读取真实输入或运行旧科学目标来冒充人工。

| 项目 | 实际值 |
|---|---:|
| 新人工 elapsed | 0.11879069300000111 s |
| 新人工 peak RSS | 28.59765625 MiB |
| 八新科学目标 elapsed | 0.217361633000003 s |
| 八新科学目标 peak RSS | 28.55078125 MiB |
| 完整新目标映射器 primitive 调用 | 3 |
| fresh 原差映射器 primitive 调用 | 3 |
| 两映射器 cycle fallback | 均 0 |
| 已监测 rational calls | 1445 |
| 已监测 rational calls 最大位数 | 9 |
| 原输入及新式合计 profile atoms | 268 |
| 逐条完整数学 stdout 字节数 | 37128 |

1445 与 9 仅统计 `MonitoredLimits.rational` 的受监测调用，不是根恢复及全部原 DAG 算术的总操作数或全局最大位数。两个映射器分别报告 peak cache 207、25，均只处理本轮新三阶导及其 fresh 原差。

临时输出的准确身份为：

| 临时内容 | 字节数 | SHA-256 |
|---|---:|---|
| 新人工 main | 4514 | `acee43e8519bdc163b2142c4e85bb21518686741f14f7d42de3d7861beec3481` |
| 完整科学 main | 37286 | `5ea4a049787fb9b3a86ea5ca9f2a737341219fdb652fc6b90c451869feb1cb2f` |
| 内存原差/伴随证据 | 13083 | `7da02709317e9b54de30eb6f0655fc8c7e10349dafc1119894e2c7284227c753` |

遵守根规则 15，新机器 payload、DAG 与证据没有保存到仓库、Release 或 artifact。全部八条数学行已在 job stdout 的 `EIGHT_KERNEL_OPERATOR` 打印，两个小报告已在 `COMPLETE_REPORT` 打印；可由已冻结源码、参数及旧输入重建。本研究目标完成不等于课题完成，报告的 `task_complete` 仍为 false。

## 7. 输入绑定与必要恢复的边界

本次只读取以下两个既有输入目录：

1. `notes/actions-43645177423-1-local_fourth_quotient` 的 W-only 原式；
2. `notes/actions-43633746055-1-full_phase_bridge_exact` 的 v2 第三模板 receipt。

第一份旧 source 为 `2f1b809c0b0abb7a26303d36940edc203815f872`，run `43645177423`。其主件 3982 B / `19228a0aecf40416cf7ba7b8a7fa4e0180ed924a4bd04435b0e6e6e4a0b1b28a`；原 publication receipt 31846 B / `c9206d68c786613e84e4f080d2a6899b46333979e88b16f0d5306a6c88e8c0ba`。

W-only 文件 `local-fourth-quotient-W-original-expressions.json.gz` 原存储 7377 B / `45cbdc8f38a4b5561924badaf9cd68a93a7fa71c6264d95489034703af4ee44a`；原展开 31750 B / `615d848611aaf787bc3ae790b4b1f81fe91338301bcb57afdfd111758cf533bf`。36 个真实原根和 170 个原 atoms 均按旧元数据绑定；旧主件的 `output_limit` 仅来自当时的大摘要上限，不是 W 导出失败。

第二份 `full-phase-bridge-exact.json` 原为 157380 B / `7c2cb9fece518fb6fbb15b6b4e034565dfcc5a10cf0e103a7011cd56dc4ac960`，run `43633746055`，source `26c3f2c0308d179a094d3967cfb7189db426081e`。本次读取其已付 152 模板来源/依赖绑定并核 36 个实际输入原根，没有重新生成 152 原式或重做旧 116 依赖。

八个完整 $\chi$ 的定义与原 SHA 来自 R254：run `43707570035`，source `282173404f65d5cc7b1dee61c66c69c3ca17866c`，job `132791905419`，当时完整主件 29457 B / `79f3fd82a22a3e24122e14f22c07fab89ebb7572048a22f9f5a8321ad1c5d11e`。本次没有恢复旧 18 个参考对角，也没有重算其 pivot 或八条 $\Delta\chi=0$。

## 8. 新局部表达与原差的逐目标身份

以下原 SHA 与完整实际逐条对应。每条局部式与其 formal adjoint 的原式 SHA 相同；fresh 原差词 SHA 均为第 4 节的公共零 SHA。

- 原索引 30：
  - 完整 χ：`e934dba9b2ee51574cdf22bb0eb1efa4f151125d2a6973c934d0b3c6942cf72c`。
  - 原 $D^3K$：`e00a5d34f833ebb7e38686df841b899437d4317c45692e4ce5bffea5729209c8`。
  - 局部算子原式（亦为 formal adjoint 原式）：`e00a5d34f833ebb7e38686df841b899437d4317c45692e4ce5bffea5729209c8`。
  - 原重构差：`4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`。
  - 完整词表示：`f4543b620b0e7ba990911790e47d911b1102b36592d4a7759b64a73525facc98`。

- 原索引 32：
  - 完整 χ：`d5eecb73427456b3075a0e93526ea5ffaee15baf902d6e72122a184cff14ee43`。
  - 原 $D^3K$：`c4064a4465041082f952ccc9bab7a081d1166a8ff3a37f2baf02f599d107cab5`。
  - 局部算子原式（亦为 formal adjoint 原式）：`e9df57a2ab60db2139245b9b9d4fd715462582aba2db21e68c38fa6ab17a5e9b`。
  - 原重构差：`46a1dbc1edd13ac4015410aebe34e49ab1043cc9ab4a9f64d1ac6a6c4fe195b5`。
  - 完整词表示：`9927cb0f4c8167bc50cdc6abed5443fa6593d09b1212b590d955d5ac484298cf`。

- 原索引 34：
  - 完整 χ：`e9711cae8ea70e3d57672acb6577e016630659235732fbb89697671d8ffdc443`。
  - 原 $D^3K$：`88a835c65234f6020e90a693716805eaec5062e251fd7daca89c0cc6b7b9a721`。
  - 局部算子原式（亦为 formal adjoint 原式）：`94881f8a7423a263a18d12194bbdc863a6723edc14750827a7bfc486a1b37876`。
  - 原重构差：`46a1dbc1edd13ac4015410aebe34e49ab1043cc9ab4a9f64d1ac6a6c4fe195b5`。
  - 完整词表示：`b006c8de441e76638ad355a13abc171bb49ebac5f46f3d3e17a44b6c11c38695`。

- 原索引 37：
  - 完整 χ：`3e262852b4a465df76bc6a3c917fb58bd30f73102b60c3b77daebdc7850a7b8f`。
  - 原 $D^3K$：`87763e8343302a007da6a2fc375de279fc6a42a9ba67306c528caa5415935f56`。
  - 局部算子原式（亦为 formal adjoint 原式）：`10a54787b90f79050a4004ac445d34972e7d5c6c40dd51fcc3ca52bb7152b246`。
  - 原重构差：`e0b60567afb7a4131e499fe13383d828d37c841bb5fa8a078296765e95477eec`。
  - 完整词表示：`ecdc89ebb70d449102edcd1fc486a75ecb083790e68f9c63f7a605bc24e4ec42`。

- 原索引 40：
  - 完整 χ：`f9cbe1f2435f9aeee4acaed8e8862832c067ea2873ba355d023b0cbf8460c71a`。
  - 原 $D^3K$：`7beecb0110949b85b6152e3a1311cd37ff38a8db957597f95a69afe990a2d6b8`。
  - 局部算子原式（亦为 formal adjoint 原式）：`35a7e631efb2623003b15104a39c8449987bfeff01aba999e2aa30e17d93d88d`。
  - 原重构差：`258d1d3757c1e69f48a1d9fb1283d40b1f4b48a6e4562b0bac49d83315e014b4`。
  - 完整词表示：`82c54e15c0fb0644263fdb266aebe5f10212c408367fa0c2d731217c553b2868`。

- 原索引 100：
  - 完整 χ：`cf0662a4a39fd1076db9ba1cdf18ec8842d6399fc3852c01e6fbfea94d262a9c`。
  - 原 $D^3K$：`df39463d3847469eaa363f38dfa368888d2cba93733807a998e01a654ae62cbe`。
  - 局部算子原式（亦为 formal adjoint 原式）：`93a5d1cad13f125789045519cc1e0cf6493ebbd486f3592187d7938643e6b559`。
  - 原重构差：`84bc67b9d18e647d29d05f93a4c97aef8de8c30e1aee72719140d48ca13fc9bb`。
  - 完整词表示：`a69b338f727dd4b6c110bd366356e433722630b938a39fec0016ac3a251c2e57`。

- 原索引 104：
  - 完整 χ：`22becb0a3bbe0dae7becd09f079f476fc923be3178653fc8acd0b09a2facd54d`。
  - 原 $D^3K$：`2ba3091137f4152b5684444e8f8cbd0ae99847389eb7fe0fa3fb60f4b1c616c6`。
  - 局部算子原式（亦为 formal adjoint 原式）：`2ba3091137f4152b5684444e8f8cbd0ae99847389eb7fe0fa3fb60f4b1c616c6`。
  - 原重构差：`4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`。
  - 完整词表示：`3631c9befea269972f0db814871fef233324f9207273e086975e9661031f3192`。

- 原索引 109：
  - 完整 χ：`6f919eb3aca85cb37f930995c088c67fed52ea44b6e0a48c1e99d1bf4c852aa6`。
  - 原 $D^3K$：`e39a6eb8230e06f18e89d8c3e36edd80750fb1c014f2c57843f8183938ce2971`。
  - 局部算子原式（亦为 formal adjoint 原式）：`e39a6eb8230e06f18e89d8c3e36edd80750fb1c014f2c57843f8183938ce2971`。
  - 原重构差：`4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`。
  - 完整词表示：`8bf8ddd965d9c2134ed97f3bd9a8bb41a008f3456e70981f2a807d35a251cee4`。

## 9. 冻结源码与完整运行参数

直接递归 source inventory 如下。此表是 consumer 的实际身份边界；工作流 metadata receipt 还记录完整 checkout 源文件，并绑定 request 的 53 个要求项。

| 直接递归源文件 | 字节数 | SHA-256 |
|---|---:|---|
| literature_c7_transverse_tail_probe.py | 11020 | `98c879d83799e275e145310f5c9fdd9b85a87503d15f1690925d2f648ebc305b` |
| literature_closed_c1_endpoint.py | 21532 | `b0c9c5a74cdc50935f97fbe1641b705155dbec82e42750393da2a34f38357bd1` |
| literature_color_priority_words.py | 21642 | `ec2022d8f9ba764dad05350b6fd2084d0c8fdc4bb9a26550f65f1f95f504a9b9` |
| literature_colored_profile_algebra.py | 15738 | `c0d87a214f27a03fb29cd07cc5e9740249580da7f854ed4ff02d6eaf69b1f66f` |
| literature_full_m8_tail_response_projection.py | 32096 | `e66bf0d2f41570526d5e6b05aedc28118a18a492a299e097d341cc71e804e345` |
| literature_full_phase_bridge_exact.py | 35368 | `d7513321bea70248851e9b71b02c97b7e869531097f290de40257c94507fed0e` |
| literature_full_phase_rational_dual.py | 19492 | `bcfb26b85918a8648ad98bbde7643c4cf6d01d34b35c53bc06c3dbaff31de84f` |
| literature_linear_third_bridge_quotient.py | 24699 | `0627875fe06950c9e7c360baaf0429451697a460e2cf10aa6b3434c501363bd2` |
| literature_local_fourth_quotient.py | 38857 | `9aa5b1360032bfebeb379d965873dc5b877c41885d8834fc1945d44d44a4dcf0` |
| literature_local_third_bridge_decompose.py | 30635 | `08ada4219df23e50dff2c784c2457dab3c732cd82cacc1477389fdc53fbb6ee0` |
| literature_pure_bulk_exact_membership.py | 33718 | `f7f3e3c6c8732ad9da047fb6005d314dc8568c189fe3cc0c9edef8843051eb70` |
| literature_pure_bulk_word_normal_form.py | 32310 | `d39482c9e33e7358f1afa51b073daf5f65e84b4858f9a18f446206e8f9d9ea65` |
| literature_range_profile_algebra.py | 33169 | `a7f1771a33a8e73934f9549b3407a9e351fed59a9eec163c5b11c965c7f1dc52` |
| literature_rational_volterra_polynomial.py | 19803 | `6bf16dd5c6cc8157fd53b20b58b504a5c3ea56ade9db9b62a30d385e5e69fd22` |
| literature_third_kernel_eight_local_operators.py | 35645 | `f59143274124c7458571f55313fca00ada93b31ee71d1be2739cbb402bbeb4d3` |
| literature_total_P1_scaling_blocks.py | 37293 | `40ff170136838907ecb4d2557c2ba3b4d06b5f3fcf63746697f3d5248e92d0fa` |

科学命令使用 runner 临时输出目录：

```text
python topics/visible-flex-new-mechanism/scripts/literature_third_kernel_eight_local_operators.py
  --w-directory topics/visible-flex-new-mechanism/notes/actions-43645177423-1-local_fourth_quotient
  --third-directory topics/visible-flex-new-mechanism/notes/actions-43633746055-1-full_phase_bridge_exact
  --output @OUT@/third-kernel-eight-local-operators.json
  --max-seconds 120 --max-memory-mib 512
  --max-nodes 300000 --max-atoms 40000 --max-terms 40000
  --max-word-calls 150000 --max-cache-entries 150000
  --max-rational-bits 8192 --max-monitored-rational-operations 1000000
  --max-proof-bytes 8000000 --max-summary-bytes 95000
  --max-mathematical-stdout-bytes 1000000
```

新增人工使用同一冻结 driver 的 `--toy-only`，输出名 `third-kernel-eight-local-operators-development.json`。完整参数原值同时保留于本次 request 与 stdout 的 main。

## 10. 对完整 period 主线的影响

本次付清了 $Z$ 的全部 hook 原局部表达，故后继可对所有十八方向统一使用自伴 Green、真实右三常数、零阶尾矩及内部退化的明确原系数，而无需再构造这些 hook 的 Volterra DAG。

仍须严格区分：

- $Z$ 是完整第三对角核；它不是整个第四 pure 零响应分支的同义词。
- 本稿给 universal 函数身份；没有计算某个固定圆上的 rank、全部平台或全部端 germ 的联合像。
- 两个 mixed 目标中的 $\zeta=K_f^\tau(g)$ 仍须保留；一般固定圆不能由逐包比例特例代替。
- 完整 period 的四类相容条件必须由同一个目标同时通过，随后同一个 gauge 还须满足完整 ruling。
- 响应线性组合的存在不自动给实际有符号成本的实现。

这些是本次结论的准确边界，而不是继续重复八个已经完成目标的理由。

