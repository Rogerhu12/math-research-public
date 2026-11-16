# 原 U·A8 完整四纤维迹的公开精确执行

日期：2026-11-16。此执行恢复的是 R884 附录C 同一特征零来源的完整系数，
不取目标素数样本，也不新增算术中央零。

## 实际运行与来源

- [公开运行 43862249339](https://github.com/Rogerhu12/math-research-public/actions/runs/43862249339)，job 133281755877；完整成功。
- source：`9dbad443f488c8cbba484ed58e7430b70e93abdf`。
- producer：[check-r884-original-u-a8-two-division-trace.py](../scripts/check-r884-original-u-a8-two-division-trace.py)；Python 标准库 Fraction，无第三方数值后端。
- script SHA256：`53cfb87bcde3d8a350a54e6ea6107afe4c29d7f93482c713d51540c8d380c5b0`。
- 完整 RESULT SHA256：`f6e8722eb41fce6c246e92a2401e9698e3de7ccc5640ff693f36e91bb1e144e9`。
- 实际输出时刻：2026-11-16 11:57:30 UTC；根/题 README blob 分别为
  `21bd547f56590b7f2dd279d0297efb289a9b2783`、
  `965ab236bbd6753acb812b45fcc36ae9b6f83b3c`。

原 workflow 为 `.github/workflows/rank2-sha-original-u-a8-trace.yml`，
在公开 Actions 内执行：
```text
python3 -u topics/rank2-sha-infinitely-many-p/scripts/check-r884-original-u-a8-two-division-trace.py
```

## 完整代数输入及结果

使用原四纤维多项式
\[
 x^4-4ax^3-8x-4a=0,\qquad (x-4a)(x^3+1)=9x.
\]
程序逐项建立全部所需正、负 Newton 幂和，再对 R884(C8) 的整个
原分子作有限二项展开。没有只取部分根或有限参数拟合。
同一次执行先恢复原 \(\mathrm T_{2,34}U=0\) 及绝对
\(\mathrm T_{2,2}A_8=-\Theta/3\)。

所得完整六系数给
\[
 \mathcal H_{36}
 =\frac{4}{2457b}\sigma^{36}
 \left(X^5+23bX^4+55b^2X^3+37b^3X^2-4b^4X-8b^5\right)
 =\boxed{\frac{4}{2457b}\sigma^{36}(X+b)^3
 (X^2+20bX-8b^2)}.
\]
一般 \(b\) 的恢复使用同一来源的齐次尺度；有限坏集仍保持。
因式式可以直接乘回全部六项，不以边界的两个值代替整多项式。

程序还以同一六行检查附录B的实际 \(A,N_{36},J_{36}\)。
这三列秩为3，加入 \(\mathcal H_{36}\) 后秩为4；
这与附录C已独立手证的单位左行相容。
取第0、1、2行确定的三列系数，在 \(b=1\) 时是
\[
 \frac5{1248},\quad-\frac5{1248},\quad-\frac1{78624};
\]
完整剩余仅在 \(X^4\) 为 \(243/2912\)，其余五行全部为零。
这准确定位新的原来源方向，没有赋原 \(\mathfrak B\) 任何新值。

原首除 \(p\) 读者仍按 R884(C17) 保留
\[
 \mathfrak B(U)+\mathscr X_p(U,\Theta^4)
 =8b\,\mathfrak B(\mathcal H_{36})
   +\mathfrak B(\mathcal U_{144}^{\mathrm{new}}).
\]
本次成功是整个固定来源恒等式的精确执行；
完整 new 项、cross、原普通/惰性中央及无穷 \(p\) 问题仍需继续。
