# 独审：体积矩通量、背景高度及修订的全相位论证

2026-11-09，`/root/independent_geometry`。审稿人未参与数值优化。尾投影嵌套子引理由本审稿人先前提出，故这里不把对该子引理的再次核对称作独立审查；其余通量恒等式、常数、脚本与背景高度证明均由未参与其推导的本审稿人审读。

## 1. 有限前缀体积矩脚本

全文审查 `scripts/db6f-root-volume-moment.py`。当前 v2 SHA256 为 `502a3d8c9439ee0b707e6be7b367e356ef44d1942aa6a0615330b1005fe10913`，实际图 metadata SHA256 为 `abf316d733c777fa07a555872c24bb1e2cf061153953874a095d77e6e5bf2a70`，数据 SHA256 为 `a98f676d5fb9b035db464a6db987df46b8e733daf127c6d794c10a3c471fac12`。

在本题目录独立运行：

```sh
python scripts/db6f-root-volume-moment.py \
  --geometry notes/2026-11-09-db6f-root-flat17-coupled-m8f16.json \
  --out notes/2026-11-09-db6f-audit-flat17-coupled-moment-v2-rerun.json \
  --angular 128 --radial 2 --batch 16
```

全部输出字段与 root v2 报告一致。冻结审查和数值账本见同名 `.json` 审稿文件。未修改过的数据只被读取，没有重新求解任何优化问题。

### 角向精确求和与取向

保存的 Cartesian 图以旋转柱坐标写作

$$w=x+iy=(R+iT)e^{i\psi},\qquad z=Z,$$

其中 $R,T,Z$ 对 $\varphi=3\psi$ 的频次最高为 $M$。于是

$$\operatorname{Re}(w^3)=(R^3-3RT^2)\cos\varphi-(3R^2T-T^3)\sin\varphi.$$

脚本的 `Xp` 是实际 Cartesian 角导数在旋转基中的坐标，包含基向量的导数；因此 `Xp[0]*Xs[1]-Xp[1]*Xs[0]` 正是 $(X_\psi\times X_s)_z$，与此前连续支持证书的外向取向相同。

乘积 $Z\operatorname{Re}(w^3)(X_\psi\times X_s)_z$ 的 $\varphi$ 频次至多 $M+(3M+1)+2M=6M+1$。均匀角节点数 $N>6M+1$ 时，离散平均精确取出有限 Fourier 多项式的零频；这里是有限多项式恒等式，不是数值求积收敛猜测。三个 $2\pi/3$ 周期合计的积分因子为 $2\pi/N$，无需再乘三。

每一角节点处的三角函数值用已审有理 Taylor 区间包围；每个径向子区间的 Fourier 系数用 Bernstein 凸包包围。径向取常区间乘精确跨度的区间包围即可控制积分。加法、乘法与总和均向外扩展。

关于 $z\mapsto-z$ 的镜像同时反转高度及外向面积向量的竖直分量，所以两个通量相同，最后乘二正确。另一个精确对称 $\psi\mapsto-\psi$ 使 $x,z$ 为偶、$y$ 为奇，故虚部通量严格为零。

原 v1 未在脚本入口排除非零 `ell`，但实际输入的 `ell=0`，其已报告数值不受影响。v2 增加 `ell=0` 和三个正整数参数的 guard，并从同一个精确 Hermite 图的最后节点，用完整高度 Fourier 绝对和给所有角向的 cut 高度区间。该新增计算已全文核对，**v2 审查及复跑 PASS**。

结果为镜像有限前缀的实通量区间

$$[0.43484892373304096,\ 0.48095522199304885],$$

以及完整 cut 高度区间

$$[1.7704697794920459,\ 1.772114271700638].$$

这些仍是有限前缀的边界贡献，不是完整实体的体积矩。

## 2. 尾部通量的条件证明

全文审读 `notes/2026-11-09-db6f-tail-volume-moment-bound.md`，SHA256 为 `e1c87d9373d9d61bab9269f0adaf6d6bc550476e6e8d965b4f1d4726c5d6ff2f`。除本审稿人参与提出的嵌套子引理外，以下部分独审 **PASS**。

由每条截面的严格星形性与 $|u|\le\varepsilon_h$，截面区域位于 $r\pm\varepsilon_h$ 的两圆盘之间。相对于 $B_r$ 的三阶复矩差因而只来自面积 $4\pi r\varepsilon_h$ 的圆环，故

$$|P(r)|\le4\pi r\varepsilon_h(r+\varepsilon_h)^3.$$

无需把材料角当作几何极角：Green 公式或水平环域的变量替换直接给

$$P'(r)=\int_0^{2\pi}\gamma^3J\,d\theta.$$

向量场 $(0,0,z(x+iy)^3)$ 的散度恰为 $(x+iy)^3$。对按正确外向取向加入的上尾，分部积分背景项并用内端圆盘的 $P(a)=0$，得到稿中的边界项 $H(c)P(c)$ 及总变差项。竖直扰动项由 $|v|\le\varepsilon_z$、$J>0$ 与水平投影面积不超过 $\pi R_*^2$ 控制。因此

$$|T|\le (|H(c)|+B_H)4\pi c\varepsilon_hR_*^3+\pi\varepsilon_zR_*^5$$

成立。若实际尾定义使用相反的参数取向，通量整体变号，绝对值界不变；最终与前缀组装时仍必须明确外向方向。上下镜像尾的边界贡献相同，合计绝对值最多为 $2|T|$。圆盘帽的水平三阶矩为零。

代入稿中有理粗界 $|H(c)|\le2$、$B_H\le1$、$c<601/1000$、$\varepsilon_h<14/100000$、$\varepsilon_z<84/100000$、$R_*<602/1000$ 及 $\pi<22/7$，用 Fraction 重新算得

$$2|T|<\frac{351967329516033}{195312500000000000}<0.003.$$

不是以浮点近似判断最后的不等式。若实际共同接口已支付，则前缀的 cut 高度界与 $|v|<0.00084$ 还立即给 $|H(c)|<2$；该绝对高度条件无需从未经认证的尾求积推断。

## 3. 背景高度总变差

全文审读 `notes/2026-11-09-db6f-tail-background-height-bound.md` 及 `closing_weighted_tail.mjs`、`closing_recalibrated_tail.mjs`、冻结 `tailnext_balanced_tail.mjs` 和 `general_root_smooth_tail_cells.cjs` 的必要公式。修订后证明 SHA256 为 `42a0c5d7019b970edc5a6b2ce2da0e1889d6aa2f3b7658c0aaa1a91fbd36b366`。**条件推导独审 PASS**。

核查要点是最后恢复段的两种 smoothstep 使用同一个外部参数。`cellSegments` 的第 7 段把 log 平台从 $0$ 过渡到 $\log\delta_0+a\log2$；`cut-preserving` 同时以 $t=S(x)$ 将 capped 与 raw 的对数坡度混合。因此不能单独断言这一段的 raw 坡度小于一，但可以准确组合为

$$\log w\le4t(1-t)-3(1-t)\le1/16.$$

cap 函数的内部七次 smoothstep 单调从零到一，截顶 primitive 的导数在 $[0,1]$，其 log 输出确实不超过 log cap。其余有限段有正 cap；第 8 段 raw 平台由 $T<27/640$ 得到 $w<5/9$；未改无限段使用已审 R15 的深源界。于是全尾 $w\le16/15$，物理宽度小于 $1/2$ 给每侧背景

$$\int|h'(r)|dr<8/15<1.$$

修订稿已明确正 caps、无 `flatOuterThroughCell` 覆盖、无 literal rejoin，且 `oldCut`、`epsilonScale` 按精确解析归一化派生。仍以精确径向归一参数 $\alpha>0$ 为条件：没有用浮点正值或保存的 Gauss 求积替代该条件的认证。

## 4. 全相位稿的修订确认

`notes/2026-11-09-db6f-all-phase-assembly.md` 新 SHA256 为 `9af3d05f9d4d2105a83e29b78970611e59ece98e051eb6574f1d6cf56c641bd6`。作者已明确 $\tau_\alpha$ 与误差拉回等式只在活动环带上使用，帽误差为零后逐块取全域 supremum；也明确实际相位区间要包含 $\pi/3$。修订处核对通过，前一审稿中其余条件论证不变。

## 5. 仍需支付的全图条件

以上论证为实际体积矩非零提供有严格余量的路径，但依赖精确公共 C² 接缝、完整闭嵌入、外向取向和同一真实背景。固定精确背景的归一化常数、完整共同 metric、全尾曲率/reach 与固定 $g$ 收敛不能从体积矩结果反推。当前文件中的 `complete_volume_moment_certified=false` 保持正确。
