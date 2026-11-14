# 对剩余前缀块对的真实角向细分

2026-11-14，geometry，AI 辅助研究。`computations/geometry_20261114_continuous_cover_budget_v3.py` 为独立入口；v1、v2 源码及实际输出保持不变。新入口保留 v2 对全部父块对的原门，只对真实失败的 prefix—prefix 父块对继续检查角子块。

## 1. 覆盖不改变曲面

原块的径向中心、径向半宽 $b_i$、角中心 $\theta_i$、角半宽 $d$ 均保持。将角区间均分为 $q$ 份；默认 $q=2$，子中心为 $\theta_i\pm d/2$，子角半宽为 $d/2$。径向中心仍是原 $s_i$，不需要新增高度均值积分点。R241 的矩形路径界给每个子块

$$h'_i=\sqrt{1+\eta}\sqrt{b_i^2+
 (a_i+L_ab_i)^2(d/q)^2}.$$

每个失败父对有 $q^2$ 个子对，必须逐一经过距离、短路径或连续法向锥门。只有所有子对都通过，父对才计为完成。原父块覆盖已支付的所有其他点对，包括尾、collar、帽及前缀—尾对，继续有效。子块边界的重叠不会漏掉任何材料点。

## 2. 新点由同一实际 PPoly 评价

对固定 $s$，实际前缀为

$$F(s,\theta)=G(s,\theta)+H(s)e_z,$$

其中 $G$ 是原物理 quintic PPoly 和原材料角反解给出的非均值表达；$H(s)$ 为旧闭组装中已算出的完整均值原函数。于是准确恒等式

$$F(s,\theta')=F(s,0)+G(s,\theta')-G(s,0)$$

给新的角子中心位置。程序用原网格的零角点保留完整原均值，并直接在新 $\theta'$ 代入原 $G$。这一步没有在两个显示点之间线性或高次插值，也没有用新的高度 gauge 代替旧场。

若存储的 $F(s,0)$ 和两个 $G$ 评价各有位置误差不超过 $\epsilon_x$，三角不等式给子中心误差不超过 $3\epsilon_x$。因此位置球半径使用 $h'_i+3\epsilon_x$。同一恒等式还在全部原角中心上重建并对照原网格位置；最大差额在输出中记录，若超过给定预算，整体数值通过标志为 false。

新法向仍由原真实 $F_s,F_\theta$ 构造。其共同高度一导来自与旧 assemble 相同的完整 1552 角规则，所以不把位置恒等式误微分成“均值导数为零”。下半片的点和法向均按原 $z$ 反射规则处理。

## 3. 可直接执行的下一轮

沿用 v2 的同一闭目录、接受前缀、公开源和原端口，只改入口：

```bash
python -u topics/visible-flex-larger-amplitude/computations/geometry_20261114_continuous_cover_budget_v3.py \
  --directory CLOSED_OUTPUT --checkpoint ACCEPTED_PREFIX.json.gz \
  --source-topic "$VISIBLE_SOURCE_TOPIC" --port ORIGINAL_PORT.json \
  --radial-stride 1 --angular-stride 1 --prefix-angular-subdivision 2 \
  --out "$RUNNER_TEMP/visible-geometry-v3/R241-cover-v3.json"
```

输出保留进入局部细分前的失败父对数、实际尝试和完成的父对数、各类子门计数、剩余子块的角坐标和余量。若某次还需要更多角细分，同一入口可增大 `--prefix-angular-subdivision`，无需改变参考度量或有限场。

v2 已通过的 $D_+$、曲率与弱标记预算保持使用原父覆盖的数值；下一轮不靠修改标记来取得新余量。源码仅完成静态审查，是否把 v2 剩余 33712 个父对全部支付，必须以公开 Actions 实际返回为准。
