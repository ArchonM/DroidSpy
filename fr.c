/*
 * Copyright 2016 CSIRO
 *
 * This file is part of Mastik.
 *
 * Mastik is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * Mastik is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with Mastik.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <assert.h>
#include "low.h"
#include "vlist.h"
#include "fr.h"

struct fr { 
  vlist_t vl;
  vlist_t evict;
};



fr_t fr_prepare() {
  fr_t rv = malloc(sizeof(struct fr));
  rv->vl = vl_new();
  rv->evict = vl_new();
  return rv;
}


int fr_monitor(fr_t fr, void *adrs) {
  assert(fr != NULL);
  assert(adrs != NULL);
  if (vl_find(fr->vl, adrs) >= 0)
    return 0;
  vl_push(fr->vl, adrs);
  return 1;
}



void fr_probe(fr_t fr, uint16_t *results) {
  assert(fr != NULL);
  assert(results != NULL);
  int l = vl_len(fr->vl);
  for (int i = 0; i < l; i++)  {
    void *adrs = vl_get(fr->vl, i);
    int res = memaccesstime(adrs);
    results[i] = res > UINT16_MAX ? UINT16_MAX : res;
    clflush(adrs);
  }
  l = vl_len(fr->evict);
  for (int i = 0; i < l; i++) 
    clflush(vl_get(fr->evict, i));
}
