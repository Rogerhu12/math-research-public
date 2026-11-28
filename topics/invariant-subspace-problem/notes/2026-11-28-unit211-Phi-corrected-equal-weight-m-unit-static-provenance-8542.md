# 修正后 Phi 图恢复 $m=u-\ell$ 单位的旧等权来源静审

日期：2026-11-28（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。

**结论：仅在当前 $\Phi=0,\ D_{\rm val}\ne0$ 原图，可以直接沿用已刊整个等权排除，支付 $m=u-\ell\ne0$。本次没有执行任何数学源、旧门、结式或证书。** 本文记录已读取的不可变对象和应用范围，不重记旧排除定理为新结果。

## 1. 原始乘法与证明链

规范结论为 [整个一般等权原排除](../results/R150-appendix-unit211-equal-weights-complete-original-exclusion.md)，blob `423e35f6b6276a5d659dd9b5a6a32727edd0a4fb`，尤其第 5 节。

已全文静读其 F243、F236、负半权自含源，以及独立 affine Gram、regular chart、y1 原源和半权的四段实际源。它们均在双点块使用

$$
\operatorname{vm}(v,w)_1=v_0w_1+v_1w_0,\qquad
\operatorname{vm}(d,d)_1=2d_0d_1.
$$

均值第 1 行使用这个真乘积，不是先前错误紧凑链中的 $d_1^2$。$N_4,P_2$、极化及原 singleton 加权值也由同一个原 Gram 构造。没有从已撤回的 $R_{\rm bad}$、旧 Phi firsthead、H42 或 583 模型取原必要性。

旧完整链是：全六生成元原迹与原 cofactor；固定 49 阶的完整 824 次 QQ 覆盖；两个大因子的固定原 52/51 阶 Gauss 返回；最后整条负半权的 QQ 原五 cofactor Bézout 1。所有固定首项退化仍包含。此次只是检查源码和证明的来源，不重新运行这些步骤。

## 2. 当前 $m=0$ 的准确映射

为免变量重名，将旧等权论文的权参数记为 $\mu$。当前

$$
L=Q-2(u-1)(u-2),\quad\ell=L/Q,\quad
m=u-\ell,\quad \rho^2=1-Q.
$$

因 $\rho\ne0$，$m=0$ 当且仅当 $b=c$。由于当前 $u-1\ne0$，

$$
m=0\quad\Longrightarrow\quad
\mu=u=\ell,\qquad Q=4-2u,\qquad
J_{\rm old}=2\mu+Q-2=2.
$$

于是旧 $T_0=-\mu J_{\rm old}=-2u$；其整 $T_0=0$ 边界在当前交图自动不存在，**本次无需把那条边界的另外依赖提升为新审查门**。

旧 $P_{02}$ 与当前同一个原值一致：

$$
P_{02}^{\rm old}
=\mu(\mu-1)(2\mu+3Q-4)
=2u(u-1)Q
=2(u-1)L.
$$

所以旧 $\mu,\mu-1,Q,Q-1,P_{02}$ 都恰由当前原单位支付。尤其 $2\mu+3Q-4=2Q$。旧两个头

$$
\delta_2=-16\mu^2(\mu-1)^2J_{\rm old}^2,\qquad
\delta_3=8(\mu-1)Q(Q-1)^2/J_{\rm old}
$$

在此处均为真单位。最终负半权的额外写法 $Q-3$ 来自 $J_{\rm old}$，$3Q-5$ 来自其 $P_{02}$，不是新增任意非零假设。

## 3. 边界分母与原不同值范围

旧源不是先倒所有几何坐标：$y=1$ 由独立原 QQ 返回排完，随后才用 $z=(x-\mu)/(y-1)$；恢复 $t$ 只除 $\mu$。$A_\mu=0$ 分为 $z=0$ 与 $z\ne0$ 全支返回，后者的 $z$ 逆只用于该支。$v=2y-1=0$、$y=0$ 都有独立原结论；首一值二次的头亦有明确原单位身份。半权 $\mu=1/2$ 的 $d,z,v,d+z^2$ 分母沿这些原边界和关系逐个支付，再由同一个首一四次及两个原 N 余式的 QQ Bézout 1 排除。

这些边界中使用的

$$
D_{\rm val}=\ell(2\lambda^2-2\lambda+1)-T^2
=bc(h-k)^2\ne0
$$

正是当前两个不同 singleton 值的物理条件。此静审没有把它推广到 $D_{\rm val}=0$ 的碰撞图，也没有把个别点集排除冒称为未局部化裸理想中的常数 1。

因此当前 $m=0$ 的全部原点都属于旧定理实际覆盖的范围，故可直接沿其第 5 节付 $m\ne0$。除这个单位外，本次不恢复任何受错误紧凑式影响的其它旧 Phi 结论。

## 4. 此次完整读取清单

下表使用实际读取内容的 Git blob；所有 SHA 都完整列出。前四项是总定理及三个完整终端原源，其余为当前应用所用边界、原定义和已有小回执。未执行其中任何源。

| 已读取对象 | Git blob |
|---|---|
| R150-appendix-unit211-equal-weights-complete-original-exclusion.md | `423e35f6b6276a5d659dd9b5a6a32727edd0a4fb` |
| 2026-11-27-unit211-equal-weight-large-factor-original-NP-Gauss-return-8542.py | `e0a04d0f4bec9c1831c65e303d3d74be57fa5732` |
| 2026-11-27-unit211-equal-weight-F236-other-original-row-cofactors-8542.py | `7e94ffc7403ec2a6bc84399dadcf86aa11e4396c` |
| 2026-11-27-unit211-equal-weight-negative-half-complete-original-return-8542.py | `3f0c4d9de90975fa2ccfab6dbeab4bc5002b8dd3` |
| R150-appendix-unit211-equal-weights-half-weight-complete-exclusion.md | `608b10104a586ca4328c3346589e22d859da213f` |
| R150-appendix-unit211-equal-weights-complete-824-degree-original-weight-cover.md | `c29d0bd60dee994487ec4943971cb8906dc4e0e8` |
| R150-appendix-unit211-equal-weights-entire-F243-original-Gauss-exclusion.md | `2efd8c1151650772c3ea24a4fc4c25646e98a243` |
| R150-appendix-unit211-equal-weights-entire-F236-original-cofactor-exclusion.md | `42f2a1a269debbc71ad8e2e0091b8df00e704787` |
| R150-appendix-unit211-equal-weights-singleton-mean-y1-exclusion.md | `b9b5224af3203568e195c7194fcf0e9fd98186b8` |
| R150-appendix-unit211-equal-weights-original-mean-leading-zero-exclusion.md | `0bf3bf2237a12b031b49fc47e0aa06389374c2bc` |
| R150-appendix-unit211-equal-weights-half-singleton-mean-exclusion.md | `83b97f0686c1740fd91179c85bdbc1f7afbb99a9` |
| R150-appendix-unit211-equal-weights-two-parameter-monic-value-quadratic.md | `8e6f28c69d83700c0a89d71ee5ca1e43967b8790` |
| R150-appendix-unit211-equal-weights-same-value-linear-remainders-and-six-projections.md | `382b283b0e2bc214cb285934280df840579a3a1d` |
| 2026-11-27-unit211-equal-weight-original-affine-quadratics-8542.js | `81c0b499b1208f6fdfd27a613f7ba1121958316d` |
| 2026-11-27-unit211-equal-weight-regular-original-chart-8542.js | `e75bc3963f8c8b847c0a6354d6dc61b666607480` |
| 2026-11-27-unit211-equal-weight-y1-original-QQ-return-8542.js | `b418a5dd71aa2300355fd98fbbdae71c6dd264ee` |
| 2026-11-27-unit211-equal-weight-half-weight-original-return-8542.js | `9e80c490ba7eb4e4191bde601bf5af9b3724175e` |
| 2026-11-27-unit211-equal-weight-half-weight-monic-remainders-8542.js | `76c1348693b3c723107c5bdaefe9d916a5442a51` |
| 2026-11-27-unit211-equal-weight-half-weight-full-resultants-8542.js | `47f4f6d5b471840c02e512796842568da3557b14` |
| 2026-11-27-unit211-equal-weight-half-weight-original-Bezout-8542.js | `85af60ac88cb63f53e4b859775d55e92f2a07c1b` |
| 2026-11-27-unit211-equal-weight-half-weight-complete-execution-8542.json | `1591bfa339c8000e4ae11b571edfee0baca2e1d2` |
| R150-appendix-unit211-equal-weights-zero-singleton-mean-exclusion.md | `a6a36e5e51249344a1615806f45d259753ff3da7` |

关键原代码的 UTF-8 SHA256：

| 原源 | SHA256 |
|---|---|
| 2026-11-27-unit211-equal-weight-large-factor-original-NP-Gauss-return-8542.py | `ae8dc73eaa338c60c83424b8ea96da55063ab826bc062e5232e40aefd50faa23` |
| 2026-11-27-unit211-equal-weight-F236-other-original-row-cofactors-8542.py | `34014ec5e9dc2dd09e222f039d42db58c4e2ffc3ed5ebb8c56b966d28f8d6eac` |
| 2026-11-27-unit211-equal-weight-negative-half-complete-original-return-8542.py | `5063af65da86c69b5d89dfd595e5a885f5b16443edd4683097e0d84f61c52e33` |
| 2026-11-27-unit211-equal-weight-original-affine-quadratics-8542.js | `88914af76ec66403312723ef45d12c2a503553007353e33d9e4774e90b7ccff1` |
| 2026-11-27-unit211-equal-weight-regular-original-chart-8542.js | `cfaa65b201c64aa7e7f019d955212b038260eb626a0b12a96856d9fd90e73e78` |
| 2026-11-27-unit211-equal-weight-y1-original-QQ-return-8542.js | `0fdc1f60daf94f572a6dbe3d623b183bde3684da1c18425161a47c9074dd2157` |

上述 SHA 只用于不可变内容定位。旧实际成功和准确失败身份仍归其原回执；本次没有新耗时、RSS、退出码或数学运行可报告。
