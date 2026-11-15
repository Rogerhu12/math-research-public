# R797：五条原低次数映射的准确 Laurent 前缀已完成

日期：2026-11-15。状态：**公开准确计算已完成。得到的是原无逆Laurent输入，不是原函数关系、极除子、β、η或规范高度。**

依据 [执行方法](../notes/R797-five-selected-original-Laurent-prefixes-method.md)、[R794 原五方向](R794-certified-original-low-degree-eta-basis.md)、[R781 原递推](R781-original-tangent-descent-and-inverse-free-Laurent-relations.md) 与 [R793 cusp及RR界](R793-original-RR-pole-divisors-and-CM-local-algebra.md)。

## 1. 五个实际完成的前缀

[公开 run43693453831](https://github.com/Rogerhu12/math-research-public/actions/runs/43693453831)，source **05bf2b2b22d1435a20233f48cb34a78fc53e7154**，成功退出0。核心证书用时 **2106.9468332799997秒**；外层回执于2026-11-15 08:48:18.791461 UTC完成。

| 原映射 | 原候选索引 | 原次数 | 普通幂 | 完整条件数N | 实际R/κ最高序号 | 实际y最高指数 |
|---|---:|---:|---:|---:|---:|---:|
| f0 | 0 | 1485 | 7 | 170 | 169 | 168 |
| f3 | 3 | 1521 | 7 | 172 | 171 | 170 |
| f1 | 1 | 1602 | 7 | 176 | 175 | 174 |
| f0+f10 | 21 | 1674 | 8 | 193 | 192 | 191 |
| f0+f4 | 15 | 1728 | 8 | 196 | 195 | 194 |

每条$y$的最低指数仍为$-1$。五条实际$\kappa$都非零，原二十cusp的分歧指数都为1；这些结论与原Hodge/相位数据逐项准确一致。系数保留原$L(t)$的完整20个$L$坐标，即**280个有理坐标**，没有仅在一个数值嵌入求系数。

## 2. 同一原输入与准确递推

每个新映射使用R794实际选中的同一Hom整数列和原六个微分。仅对R774已成的共同56个Hodge三积作该新标量收缩，保留原$4/1722^3$、原重数、一次$q_Y$移位及$q_Y=\xi^{10}v$的原相位。原$f_4$、共同Hodge三积、period、Hom和旧Fourier系数没有重算。

每条归一化仍为
$$
y_g(v)=-\frac1{246^3}\sum_{r\ge0}
R_{g,r}\kappa_g^{-(r+1)}v^{r-1},\qquad R_{g,0}=1.
$$
实际运行沿R781的无逆递推，保存各阶完整原字段状态及前阶SHA；阶$n>0$仅除原非零整数$3n+1$。每个保存阶段都准确验证其原微分恒等式。没有求代数$\kappa^{-1}$，没有重施$c_1$相位或实下降三同源。

每条只生成自身需要的$N$个R阶段，旧$f_4$及超出各自界的项没有生成。907个逐阶Laurent状态，加五份新scalar、五份原H3输入、五份完成prefix，共922个阶段。原输入的H3界为各自N，所需原real相位全通过。

## 3. 后继还必须补的一项

完整原关系为
$$
246^3\kappa_g^{n+2}A_n+
\sum_{j=0}^{n+1}\kappa_g^j R_{g,n-j+1}B_j=0,
\quad -1\le n\le N-2,\quad A_{-1}=0.
$$
最高一式的第一项需要$\kappa_g^N$，而本次实际保存到$\kappa_g^{N-1}$。
[R801](R801-original-minimal-long-tails-and-exact-relation-interface.md)已证明后继只需增加一次
$$
\kappa_g^N=\kappa_g\,\kappa_g^{N-1}.
$$
必须绑定各自原$\kappa$，不能借用旧$f_4$，也不能为此重跑$R_{g,N}$或额外H3项。这里如实区分“完整所需Laurent已成”和“所有清行幂已齐”。

## 4. 源码、参数和完整来源

| 项目 | 完整绑定 |
|---|---|
| 核心 | scripts/R797_five_original_Laurent_prefixes.py |
| 核心SHA | fd3bfd286b587dba76283cbfe6e56244eef6ce5248a91e9457988bccde051086 |
| wrapper | scripts/R797_public_five_original_Laurent_prefixes.py |
| wrapper SHA | aa795f1c3f5c1ab5de992d8c4bfb7950f5c63e2e779ff566c2474364a99d5f75 |
| 方法SHA | 15668e4a9e695f7d33aa222d725995927f047f55d8e31e7df209628a1d3953ad |
| 实际请求 | notes/R797-public-five-original-Laurent-prefixes-request.json |
| 请求SHA | 7c24f2e5460a28e19a3569ac4683044a1046343ce8d8a5f88d001eb9629eae19 |
| 原R781递推核心SHA | d024a7a6f5febd4658e8b5b5e5e3659f3c5fcc0daa39d70569ac408ef83a8751 |
| workflow | .github/workflows/serre-p41-five-original-Laurent-prefixes.yml |

实际请求固定原候选[0,3,1,21,15]和上表逐映射界，预算300分钟。直接输入为R774/run43631427773的62项及R794/run43691270124的6项；只有新五条微分需要的56三积、原模型见证和新选中方向输入，未把旧$f_4$的H3/Laurent重复带入新算术。

## 5. 证书与完整文件清单

| 输出 | 字节数 | SHA-256 |
|---|---:|---|
| p41-five-original-low-degree-Laurent-prefixes-certificate.json | 9045 | f41ee0a2f5e834fdd89823ddd3fc60df8cd309cd7ffb96aefa511b81068f91ce |
| R797-Laurent-stages-manifest.json.gz | 51188 | b04a902bdb1cfaa3967c45e948bfdb1146f37cb87f309bb8ebf52b7e767e9f50 |
| full-outputs-manifest.json | 287840 | f22cdd2385e8cf31e884884f4b9870d50bad99b803f696146ca0ccffd1db6e83 |
| R797-map-000-complete-prefix.json.gz | 12949 | 6946f160f42ad0b8f184a59b8e43d02b02cfdb564e9071bb97ba352f73a4cccf |
| R797-map-003-complete-prefix.json.gz | 13085 | 6cdf62bc6245c3fbb7a1a0a72a07a2ad5857133eeb76914c1d4547e2128b0e8a |
| R797-map-001-complete-prefix.json.gz | 13291 | 3b9892ec10c7e684d2b08d1456a003038ec414a45ad057cca3bc1e274f43ffee |
| R797-map-021-complete-prefix.json.gz | 14224 | 7f1a72d3bb8cf07f9ca29436d61d91508138da8730fb2b7c876f1271e50f45e8 |
| R797-map-015-complete-prefix.json.gz | 14350 | 12bd0cefdba1aec52fbb51f1db3033ff63f0864871e332ffa5a8493743feab77 |

完整manifest共**930个输出文件**，stage manifest共**922项**。原artifact **14154283549**，名serre-global-R797-five-original-low-degree-Laurent-prefixes-43693453831-1；ZIP **902836624字节**，SHA-256 **d140f4ff8101a87c000e16babcf9b2ed9520b39852b1e4ad16ddc36899b315dd**，保留至2026-11-16 08:48:19 UTC。

[公开纯IO run43699442183](https://github.com/Rogerhu12/math-research-public/actions/runs/43699442183)，source d9c4795a140a6815253f079eaf7936ac096a92ad，于09:29:38 UTC完成原ZIP SHA、全部文件字节数/SHA、原source/request/core/wrapper及原wrapper verify(item,out)检查。922阶段各自的完整tag、原前后SHA链、每阶280坐标长度与准确验证标记均读取通过；没有重新执行递推。12445字节IO摘要SHA为eadb07f507dc196f8e3ab356b5b5f40eb58f0b9e64830c469f2305377ce2a40d，保在一日artifact14156101148。

## 6. 边界

每条实际prefix可按其完成证书和原阶段链独立消费。它不表示关系矩阵的核已经求出，也没有把原Laurent写成全球A/B。

R799短基和R800新M2尾已成；R801只补缺失长尾，原函数关系与极除子仍须真实输入和实际计算。另一条原共轭加法路线可复用这些数据，但不使本结果失效，也不授权重算旧前缀。

全部可重算坐标、阶段和原输入仅用当前一日artifact/bundle续传；Git/Release只保脚本、参数、run/source、结论和输出SHA。
