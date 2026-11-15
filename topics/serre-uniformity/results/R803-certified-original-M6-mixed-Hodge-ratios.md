# R803 原694维 M6 混合 Hodge 比值的实际认证

日期：2026-11-15。状态：**已证明，原准确坐标已由公开 Actions 实际计算并完整核对。**

本结果完成 [R803 原单映射复用证明](R803-original-single-map-reuse-and-mixed-Hodge-ratios.md)
§§2–4 的有限计算。原 $Y,K,L=K(b),s=1+2\zeta$、原 $f=f_4$、
原 $T$、Hodge 微分、尺度和 basis recipe 均保持。

## 1. 实际得到的六个同权形式

用原规范
$$
h_f=2\pi iH_f\,d\tau,\qquad
h_j^{\rm map}=(T^jf)^*\omega_C=2\pi iH_j^{\rm map}\,d\tau
$$
定义
$$
U_0=H_f^3,\qquad U_j=H_j^{\rm map}H_f^2\quad(1\le j\le5).
$$
本次已经准确算出六个 $U_j$ 在原完整694维 M6 基中的全部坐标，并认证
$$
\frac{h_j^{\rm map}}{h_f}=\frac{U_j}{U_0}\in L(Y),\qquad1\le j\le5.
$$
$U_0\ne0$ 沿原 R774 完整证书，不需要选其立方根。

系数域14个有理坐标按原顺序
$$
1,b,\ldots,b^6;\quad s,sb,\ldots,sb^6,
$$
其中 $b$ 是原模型参数，不换成别的同构模型。
输出同时保存整数尺度基 $\widehat F_a=82^6F_a$ 的系数和原无尺度 $F_a$ 的系数；
$82^6=304006671424$，两套系数依 R803 (803.17) 准确转换，
没有把分母或尺度置1。

## 2. 原基与完整认证界

原空间为
$$
M_6(Y)=H^0(3H+2(P_0+P_1)),\qquad\deg=820,\quad\dim=694.
$$
前690条是原 R786 普通 V3 行，全部直接读取。
后四条严格沿 R775 保存的原 recipe：

| 原行号 | 无尺度形式 | 此处整数尺度形式 |
|---:|---|---|
| 690 | $E_4T_0$ | $82^4E_4e_0$ |
| 691 | $E_4T_{73}$ | $82^4E_4e_{73}$ |
| 692 | $E_6$ | $82^6E_6$ |
| 693 | $\eta_{\rm Ded}^{12}$ | $82^6\eta_{\rm Ded}^{12}$ |

在0至41项，$E_4=E_6=1$，$\eta_{\rm Ded}^{12}=q_Y^{41}$。
这一步只补四条原 recipe；没有重新计算旧 E1、M2、普通 V3 或旧 Hodge 三积。

使用完整42项以及原 $\mathbb Q(\xi)$ 的40坐标，得到同一个
$1680\times694$ 有理整数矩阵。R803 定理803.1证明该前缀单射：
42项消失在原20次 cusp 上给至少840个零，超过820。
因此每组的全部1680行准确代回结合原生成性，认证原全球同权截面等式；
不能仅凭694个选行的拟合断言成员关系。

## 3. 真实694块、84右端与有理恢复

实际选中的辅助素数及 determinant 是
$$
\ell=1000000007,\qquad\operatorname{rank}=694,\qquad
\det A_I\bmod\ell=637607829\ne0.
$$
原694行集、模逆及乘回单位矩阵认证均在实际 short-minor stage；
本次未形成694阶特征零有理逆。

六个 $U_j$ 各拆成14条有理右端，共84条。
全部六组都在368个 Dixon 位完成，有理重构模数的十进制位数均3313。
每次重构采用共同严格矩形界 $2AB<M$，恢复原右端有理尺度后，
每组694×14坐标**全部在原1680行准确代回**。
分母保留在原输出中，没有把有限域坐标当作有理坐标。

| $j$ | 实际 Dixon 位数 | 坐标 stage | bytes | SHA-256 |
|---:|---:|---|---:|---|
| 0 | 368 | `R803-exact-original-M6-coordinates-j0.json.gz` | 22718791 | `f27e4d9feaed1da3b4d2ecf9cd87c4c4e7bae11a59b82d5b4d08ba00862ec361` |
| 1 | 368 | `R803-exact-original-M6-coordinates-j1.json.gz` | 27211888 | `8240d4bc64f11d7abf244bd5f2fd685015c93e95ce7c63b220762d0e540a6fc5` |
| 2 | 368 | `R803-exact-original-M6-coordinates-j2.json.gz` | 27261283 | `c96fe58c2dde1eea2e9c78bfc48caccb24eb05ccfff5fc6993e483edec419d09` |
| 3 | 368 | `R803-exact-original-M6-coordinates-j3.json.gz` | 26944138 | `f3c99137fd101682ca12f467c8d3edeb9329a5f27f763771b8beb38934c2ad6a` |
| 4 | 368 | `R803-exact-original-M6-coordinates-j4.json.gz` | 27307626 | `4584ee0705fe68a4070f5a9cf2c5711ae852b4719bb30bad01a941983df5be4c` |
| 5 | 368 | `R803-exact-original-M6-coordinates-j5.json.gz` | 27322962 | `6d0df6971d1d1b1654d579e284c3b2ca6b50e09cbfc533db1181efaeb1c99491` |

六组使用同一个原694块。$U_0$ 读原 R774 已成块；
另外五个 $U_j$ 只按原混合重数收缩旧56张量，并保留
$4q_Y/1722^3$、原 $b,s$ 乘法及原 $T^je_4$ 微分列。
不能给混合三积误套纯立方的1、3、6重数。

## 4. 运行与冻结来源

- producer source：`2a3f5be764ecd335e7980557800d15959574bc8e`。
- producer run：[43702905620](https://github.com/Rogerhu12/math-research-public/actions/runs/43702905620)，attempt1，success。
- 实际核心耗时：2127.991745813 秒。
- [数学核心](../scripts/R803_original_M6_mixed_Hodge_ratios.py) SHA：`1233536f55fdcddad3fe1c48396fb32bcdee787a3f2df5d193f1b9472d4b1531`。
- [执行wrapper](../scripts/R803_public_original_M6_mixed_Hodge_ratios.py) SHA：`b8cedc8f8ddbf43bda56f0f761b3b6f54ce21b1271bce9a78a0d5ee5221fd188`。
- proof SHA：`1ef5f2a2be080e28f83551003aa18479b032d39bbe2c87cf1c65df0e69945ac0`。
- [方法契约](../notes/R803-original-M6-mixed-ratios-and-addition-interface.md) SHA：
  `b1e71dfce3e5ddb4219ad94526c23de132f2d13dfdc9461398c16ce1079c42c0`。
- [原激活请求](../notes/R803-public-original-M6-mixed-Hodge-ratios-request.json) SHA：
  `1e04be73689e0a88799b0d5363c3a691ae765e448ffce1e34ee2273806486346`。
- workflow `.github/workflows/serre-p41-original-M6-mixed-Hodge-ratios.yml` SHA：
  `457c3bdc8153068f40b3b012bd097d7b63b2f512da0276490d6de7ef42807c30`。

参数按该 source 的请求固定：p41、42项、完整1680行、原M6维694、
六组原14坐标、同一原694块和严格有理重构；
预算300分钟。本次实际完成，无需继续任何本次 Dixon 断点。

## 5. 实际全输出与原输入审核

原artifact `14158313322`，
`serre-global-R803-original-M6-mixed-Hodge-ratios-43702905620-1`，
ZIP 196959640 bytes，
SHA `726bc2dc20031eb956000d7b8053f07865d628047fd9c248f986a90059dded42`，
临时有效至 2026-11-16T10:47:43Z。

公开纯IO审核 run
[43707079568](https://github.com/Rogerhu12/math-research-public/actions/runs/43707079568)，
source `f59c795c69c05bed6efa45a937ab352def8e5972`，
采用 [`R803_public_success_io_audit.py`](../scripts/R803_public_success_io_audit.py)，
SHA `04a4777e6567c6a181f1bda449e498904f2b8fe011c8c442b578466614edea40`。
实际下载ZIP并逐个核31个manifest项的尺寸和SHA，ZIP共33个文件，
23个数学stage。manifest登记文件未压缩总量 196938933 bytes。

原输入包 `R803-retained-producer-inputs.tar.gz`，
31809572 bytes，
SHA `ae07b58d064db03624af9f4dd11dac722998cc28f751438e30fcd661088afb22`。
781个实际包成员全部按原manifest核对：

| producer | 原run | 实际消费文件数 |
|---|---:|---:|
| R759 | 43625474728 | 6 |
| R774 | 43631427773 | 64 |
| R775 | 43679160495 | 6 |
| R786 | 43682100611 | 698 |
| R794 | 43691270124 | 7 |

审核从 producer source 逐个读取冻结核心、wrapper、proof、method、request、
helpers、workflow、两README并核SHA，然后直接调用未修改的原输入选择及verify，
返回0。没有导入数学核或flint，没有重新做 Dixon；
完整准确等式由该次原核心实际执行，审核核实其原始产物、所有来源和认证字段。

| 关键文件 | bytes | SHA-256 |
|---|---:|---|
| `p41-original-M6-mixed-Hodge-ratios-certificate.json` | 10706 | `9b2854acad8e71a92ae35b8a52b5695ad9609910729a3f4b21c21a8eba7a526b` |
| `full-outputs-manifest.json` | 10982 | `c799e14e84cf83b667a9aff4b573821c43aabc57dd88bee588799d314a305729` |
| `R803-stage-manifest.json.gz` | 3862 | `cb74c94648b3352ee3100b8f960405428ebd26f37a565a15669736cfcd05ac3a` |
| `R803-original-M6-short-basis-index.json.gz` | 44362 | `e195e500775b6afa15f4bfc93011be99dbb6fd9b37817b769a7d4f15568f223d` |
| `R803-prime-1000000007-short-minor.json.gz` | 2182448 | `20a0f83a06a675566435540cfe4b0985759c18cef20de666dcc56402adefd3a4` |
| `R803-original-mixed-Hodge-ratio-interface.json.gz` | 3330 | `71c601b453052602e61d70c0c8d0a9209bb3035c3bf115601f07f1b58034c86c` |

完整IO摘要 SHA `1ec4dfc4772d8052150e6d47c92167530e57ea5d6f99193acc0f007fa4a3353c`，
在该审核run日志和一日临时artifact中。
大坐标stage不重复上传，不写Git或Release；消费者直接读取原成功artifact。

## 6. 直接后继与边界

R803 原证明 (803.18)–(803.22) 现在只差原 $u=y_f=A/B$ 的实际求解，
即可用这五个已成比值和原 $\rho_j,\sigma$ 指定五条完整加法函数。
正在运行的 R787 保持原核心和断点身份，不为本次成功重开另一份函数求解。

R807 的一次 $\theta$ 清极可独立进行：普通690项仍沿原截面环乘法，
四条额外行消费它的全1100行坐标。这不需要重解此处84条右端。

原真norm与同靶乘积之间的 $b^7/N_{L/K}(b)$、原三同源常数、
R794列变换、反实 $\Lambda/s$ 和主函数标量继续按原证明保留。
本次没有实际 $y_g$ 函数、极理想、KM代表、$\eta$、
对称线丛二挠比较、$c_0$ 刚性化或规范高度。
有限p41输入完成也不等于 Serre一致性主问题完成；主目标仍OPEN。

审核中的真实部分clone及pull于
`2026-11-15T11:04:01.494034+00:00` 完成，HEAD/origin main为
`f59c795c69c05bed6efa45a937ab352def8e5972`，两README相对此前已读提交没有变化。
