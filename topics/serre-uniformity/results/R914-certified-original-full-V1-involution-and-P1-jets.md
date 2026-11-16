# R914：原完整 V1 几何反射与 P1 的273项正常 jets 已认证

日期：2026-11-16。状态：**真实公开 Actions 已成功；以下登记该次实际产物，不增加一次数学执行。**

本结果完成 [R912](R912-original-eight-dimensional-endpoint-lattices-and-norm-frames.md) §2 的必要源：原146维 $V_1$ 的完整准确几何 involution、原 $P_1$ 的272个正常函数在指定参数下第0至272阶 jets，以及原 $t-1$ 帧的首项。它不把原 R885 的 $z=0$ 纤维当作端点，不计算八阶端点 order、目标九 Norm、Poincaré period 或高度。

## 1. 实际执行身份

| 项目 | 原实际值 |
|---|---|
| repository | `Rogerhu12/math-research-public` |
| source commit | `1b397d402ac0d6ff5872f77c1409fba356ff77c6` |
| workflow run | `43898224893` |
| actual construct job | `133407590978` |
| rules job | `133407498050`，success |
| result | `R914-original-full-V1-involution-and-P1-local-jets` |
| core | `R914_original_full_V1_involution_and_P1_jets.py` |
| core SHA-256 | `c7dded45af13c7cd37b9c5261d917c2e81d3c179debe963296bbd8caf746e004` |
| wrapper SHA-256 | `a6a26387e76bbd6387aa47d7bb90384e3a3ccc129f09f4717bb2ec4e1098a206` |
| execution method SHA-256 | `8c8d188627c69d720d83e166403f9ba8f3b23c51dc46d28a2c11890bdf66a897` |
| actual request SHA-256 | `59cae2f02c930b6cc08bce19a4e3ea95502465517a5d048f328685943c0de46a` |
| R912 proof SHA-256 | `273ef827c365b7901f349150f0665cffd57e330e2806dd8113649b3482671e97` |
| actual configuration SHA-256 | `feb2b20f1e95bd9be878d47b2045b4da57352489c24c02f3ac1bce8ab0b2a432` |
| mathematical exit | `0`，error null，complete true |
| core receipt seconds | `0.6583013830000084` |
| actual complete mathematical stages | `26` |

上表的 proof pin 以实际 request 的逐字字段为准；来源闭包和全部输出由下述原 manifest 绑定。公开执行链接为 [run](https://github.com/Rogerhu12/math-research-public/actions/runs/43898224893) 和 [construct job](https://github.com/Rogerhu12/math-research-public/actions/runs/43898224893/job/133407590978)。core、输入和输出身份均未冒用旧 producer。

最终证书 `p41-original-full-V1-involution-and-P1-jets-certificate.json` 为 **13,921 B**，SHA-256：

`8c2ce53f706174878076587879cff870abb3549783145156295f4601ae3bbdb0`。

原 `core-receipt.json` SHA-256 为 `a9862724d63459c363828142ca198a019c987b37eb6e6b50fe814b211d778b42`；run receipt 明确 source、exit0、非 outer timeout，绑定该 core receipt。

## 2. 完整准确的原几何 involution

保持 [R802](R802-original-semilinear-parity-and-degree-seven-relations.md)、[R837](R837-certified-original-P0-evaluation-and-fixed-branch-pencil.md) 与 [R853](R853-certified-original-three-V1-conjugates-and-semilinear-generators.md) 的原定义。原整数截面为

$$
e_i=82^2T_{1,i}.
\tag{914R.1}
$$

输入矩阵 $S$ 直接读取这些原 $e_i$ 的560个 $q_Y^n\xi^r$ 坐标，$0\le n\le13$、$0\le r<40$。没有再次乘 $82^2$。原几何反射 $ι=T^{41}$ 在本 $K$ 模型上固定系数，作用为 $q_Y\mapsto-q_Y$；它与包含系数共轭的算术 $c_Y$ 保持区别。

本次读取原 R837 的准确146行非零子式，复用 R853 三个已经完成的准确 RHS。其余**143个**原 RHS 在公开 Actions 中解出；使用原线性关系 $σ=e_1+e_{73}$ 恢复第73列，不再解旧三列。实际输出整个 $146\times146$ 有理坐标矩阵 $C_ι$，并完成

$$
SC_ι=DS,\qquad D_{(n,r),(n,r)}=(-1)^n,\qquad
C_ι^2=I_{146}.
\tag{914R.2}
$$

原验证 stage 明确记录**81,760条**准确 Fourier 方程全部通过、完整平方为单位、原三条回答和 $τ,w_0$ 固定均保留。结合原 Fourier 评价单射，这就是原几何作用，不是从模平方猜出的 involution。

关键原件：

| 原件 | bytes | SHA-256 |
|---|---:|---|
| `R914-iota-exact-V1-coordinate-matrix.json.gz` | 186622 | `b44a59af06cb745eca1b7bef41513b81f59ce29f425ae303bc4e93bb53047667` |
| `R914-iota-exact-full-V1-action-verification.json.gz` | 3923 | `37a9ef48e037df79aab868204401bfea0cc3228b4820b423718ea3652e47b87c` |
| `R914-iota-original-p753-coordinate-matrix.json.gz` | 32613 | `91030a7524c70ad4740c578feac9e58a0a5053eb047940ab6a36a34e13b4fbc2` |

第一项是准确有理矩阵；第三项只是它在原合法地方的减模，二者不混名。

## 3. 原 P1 的完整正常 jets

原 R872 实际参数为 $ρ_0=z-z(P_0)$。本次固定

$$
ρ_1=ι^*ρ_0=z-2β_{72}-z(P_0).
\tag{914R.3}
$$

它没有被换成 $z-z(P_1)$。原 $P_1=ι(P_0)$ 的零阶值用原 CM 值作准确校核；原146截面基与272正常基的区别、$e_1/τ=z-β_{72}$ 与 $e_{73}/τ=β_{72}$ 的双重坐标均保留。

本次读取原 R872 已成273系数，用完整 $C_ι$ 运输整个146列，再按原 R805 的 degree0/1/2 正常 recipe 得到272个正常函数在 $ρ_1$ 下的273项。实际辅助地方固定

$$
\ell=1000000753, \qquad ζ=549966761, \qquad s=99932770.
\tag{914R.4}
$$

所有保存的正阶数组都是原准确运输定义的合法减模；本结果没有展开其特征零全部正阶有理系数，也不是原 $p=41$ 的数值 period。

| 原件 | bytes | SHA-256 |
|---|---:|---|
| `R914-iota-original-P0-V1-jets.json.gz` | 205777 | `b0d5137d3ddeb3df57570782b308729583f7c052d905f6b3113de968a39c9c44` |
| `R914-iota-P1-V1-jets.json.gz` | 205866 | `055ffec11eedc141e49f0a023eb13b63b7a18e6ba36db20e2d2d95bd03b9dcf7` |
| `R914-iota-exact-original-P1-point-and-zero-order.json.gz` | 8592 | `c2cab789f3a141ccd36307ed8bca82e34ac30e9eedf38603bb2bd77b2f14173c` |
| `R914-iota-P1-normal-jets-index.json.gz` | 4979 | `d73826726d8a8fcd84d7d7eaac250938e7cc58c730fcab657c2b8af8b9ae9c99` |

正常 jets 索引逐字绑定 `R914-iota-P1-normal-jets-group-000.json.gz` 至 `016` 的17组，每组16个原正常函数，合272。原源的 W、Hensel 方程、旧273项、旧反射子式和旧三 RHS 均未重做。

## 4. 原 t 帧及其符号已实际保存

原几何恒等式 $ι^*t=1-t$ 和 (914R.3) 给

$$
t=c_0ρ_0+O(ρ_0^2), \qquad
t-1=-c_0ρ_1+O(ρ_1^2).
\tag{914R.5}
$$

原 R883 准确表达式

$$
c_0=\frac{a_1b_0-a_0b_1}{48s b_0^2}
\tag{914R.6}
$$

及其原 $N_{692},N_{693}$ jets 来源原样保存。实际原地方的输出是

$$
c_0=354813668, \qquad c_1=645187085,
\tag{914R.7}
$$

并保存 $t_1=t-1$ 在 $ρ_1$ 下前三系数

$$
[0, 645187085, 930983616]\pmod{1000000753}.
\tag{914R.8}
$$

没有计算273个 $t_1$ 系数，也没有引入新 CM 周期。对任意有符号整数 $m$，原帧变换保为

$$
Lρ_1^m=(Lc_1^{-m})t_1^m(1+O(t_1)).
\tag{914R.9}
$$

所以负极阶仍对应正 $c_1$ 幂。实际原件 `R914-iota-original-P1-parameter-and-t-frame.json.gz` 为 **4816 B**，SHA-256 `75f5ae4757ad0acbd00a5d8243818aa434eb0846dcb323b49c665c07498d8c45`。

## 5. 原来源闭包和一日 artifact

本次实际消费469个原件，分组为 R786 152、R805 7、R837 9、R853 9、R872 282、R883 10。R837 的来源是两个已有载体中的同一原 producer 选件合并；没有要求过期原 artifact。全部原 tag、file/bytes/SHA 和未再次缩放的基序由 source audit 固定。

- source audit：`R914-iota-source-audit.json.gz`，27882 B，`1cde5642174ddab449b1df273cdcdd654d52c6be789585a304e932c6940e02fd`。
- 原输入载体：`R914-retained-original-inputs.tar.gz`，5251942 B，`0a5517ec0d87734d7500872771d430caa25eb73b4c2454e1a3715b69e3a8bee3`。
- 原来源 inventory：`R914-original-source-inventory.json`，81339 B，`cb7e1469d06e5d28ecd6135efc823a534cc0e683a5070b32ef4ad916da8747ec`。
- 完成数学 manifest：`R914-iota-stage-manifest.json.gz`，4995 B，`d29da4d32d75f22e76af1101c46e569aea4aa2abc8f9ae0522e93febc07fad80`，列26个完整数学阶段。
- full manifest：`full-outputs-manifest.json`，6251 B，`fbc71afa26e27789c02814da7004db2b442bd2312441c22a3e9303d63e8b3f36`，列37件上传输出。

真实 artifact `14241065505`，名称 `serre-R914-full-V1-involution-and-P1-jets-43898224893-1`，ZIP为 **6,647,816 B**，SHA-256 `94eba2eaa86ad7ee48796b6d93d7df39b637b260683d08970488150848f91bee`；平台到期时间 `2026-11-17T15:37:49Z`。

结束纯 IO 已下载并核完整小 ZIP，39个 ZIP 成员恰为37个 manifest 输出和两份 manifest/reference；其后逐字核469个原载体成员。该读取没有执行任何矩阵、jet 或数学核心。完整原结果与原始数学数据保存在一日 artifact，不写入 Git。

## 6. 本次可消费出口与未成部分

后继可以直接消费：准确 $C_ι$、全560行准确验证、两个原146叶 jet 矩阵、$P_1$ 全272正常 jets、准确 CM 零阶及原 $c_1=-c_0$ 的来源标记。

最终证书的三个本次目标旗标全部为 true：完整146准确几何反射、原 $P_1$ 正常 jets 第0至272阶、原 $P_1$ 的 $t$ 首项单位。其余边界仍为 false：完整272维半线性作用矩阵、秩八端点整代数、九 Norm 的两个端点标定、完整 $\operatorname{Nm}(q^*\Phi)\det U$ 和参考帧数值、Poincaré period/theta/高度。这些不得由本次反射与 jets 成功代替。
