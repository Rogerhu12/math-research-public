# 原固定背景：保留已完成36剖面，准确补齐到depth8

日期：2026-11-28；会话：Astra-visible-flex-2ecfcd69-20261128。

为了覆盖原18552个有限尾部单元，原depth4背景primitive的36个剖面不足。此条只补原输入的缺失剖面，不改变目标g，不重做已登记36个剖面的积分，也不凭空重造已不在本地的旧checkpoint。

## 原输入与保留事实

实际输入是已完成的 `2026-11-09-db6f-tail-background-primitive-stable-depth4.json.gz`，SHA256 `28577da04035f91bcd5dc310094d5844347cbeb78d6213dcba0232b62acf56e9`。其中已保存的完整冻结参数配方原样保留。新入口实际核其所有source实现SHA，以及原calibrations、tight-alpha、cell-zero A、inner-A、outer-B的各自SHA与checkpoint/calibration绑定。三份积分报告和alpha报告绑定的原checkpoint都是 `d23b03e4ce5cd7aaf4ac9d1134f8a23ee274be3a1d0a0192a7b294f1195e43f0`；这里不把任何新JSON冒作这个checkpoint。

新depth8强anchor按原准确积分报告重新组合；所有旧36个anchor与原表逐值相同。已有36个profile直接保留，随后仅用原 `FrozenSource` 和 `build_profile` 生成 n=4,5,6,7、每层j=0..8共36个新profile。order=8、density=1e−10沿原设置。终态再次核旧36个完整profile完全相等、全部(n,j)集合恰为0≤n<8、0≤j<9。

## 实际返回及范围

入口自然exit0，新增计算117.708914728秒，最终72个profile、`finished=true`。输出 `original-tail-background-primitive-depth8.json.gz` 为2045031bytes，SHA256 `9f208c790470849af024bc15ac8bb961edc5dfb02f97332a1abef8b9a5a8c264`。新时间位于 `extension.seconds`；父对象旧 `seconds` 字段按原对象继承，不能当作本轮总墙时。

最内profile的左anchor区间下端约0.1525361819533974，外端0.6。原有限尾的准确内端约0.1525361819534748；二者不是同一个精确数。后续背景消费者用原有准确anchor区间、逆函数残差及全局物理Lipschitz界包住这段不确定性，不能把anchor下端直接宣布为原source单元端点。真正cuff r=0.15到原有限内端的闭合区间仍须另付。

父报告遗留的 `pending-independent-review` 字样只是原状态字段；根README§13已取消旧额外复核门，此条不将它重立为完成条件。新的extension字段明确列出全部真实追加剖面和已核身份。

## 可重生入口

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python scripts/2ecf-m12-extend-original-background-primitive.py --scripts scripts --parent <original-depth4-primitive.json.gz> --depth 8 --out /tmp/original-background-depth8.json.gz
```

入口SHA256 `0e6534516efc50b2d4312a7cf505433285ea6e27804a256aaa428e7f9035314c`。原depth4的配方和来源仍沿原登记；大primitive只保留临时本地，可按以上原源参数重生，不入Git或Release。该表自身不是完整曲面metric/reach证书。
